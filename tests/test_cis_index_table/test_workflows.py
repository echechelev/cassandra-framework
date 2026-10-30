import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("📥 Полный успешный цикл сканирования и добавления в архив")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.workflows
def test_full_scan_to_archive(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету "TEEGARDEN C".
    4. Нажать на кнопку "ANALYZE CIS" и дождаться окончания сканирования.
    5. Нажать на кнопку 'Add planet'.
    6. Выбрать планету "TEEGARDEN B".
    7. Нажать на кнопку "ANALYZE CIS" и дождаться окончания сканирования.
    8. Проверить: в зоне выдачи появились 2 записи.
    9. Проверить: записи отсортированы по % CIS, первая "TEEGARDEN B", вторая "TEEGARDEN C".
    10. Проверить: кнопка "ANALYZE CIS" заблокирована - "DISABLEAD"
    11. Проверить текст телеметрии - "SCAN COMPLETE: TEEGARDEN B — CIS 55.6%".
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.TEEGARDEN_C_NAME)
    cis_index.click_analyze_cis()
    cis_index.click_add_planet()
    cis_index.select_planet(data.TEEGARDEN_B_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.verify_planet_in_archive(data.TEEGARDEN_C_NAME)
    cis_index.verify_planet_in_archive(data.TEEGARDEN_B_NAME)
    cis_index.verify_archive_sorted_by_score_descending()
    cis_index.verify_button_state(element=cis_index.analyze_cis_btn, is_enabled=False)
    cis_index.verify_text(
        element=cis_index.system_telemetry,
        expected_text=data.GREEN_TELEMETRY_CIS_SCAN_COMPLETE_TEEGARDEN_B,
    )


@allure.id("CAS-02")
@allure.title("⏹️ Полный успешный цикл сканирования и добавления в архив")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.workflows
def test_cancel_scan_and_reset(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Выбрать планету "MERCURY".
    3. Нажать кнопку "Add planet".
    4. Выбрать планету "VENUS".
    5. Проверить имя планеты в заголовке зоны сканирования - VENUS.
    6. Проверить: зона выдачи в архиве содержит запись "NO SCANS IN ARCHIVE".
    7. Проверить текст телеметрии - "TARGET ACQUIRED: VENUS. DATA LOADED. READY FOR SCAN.".
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.MERCURY_NAME)
    cis_index.click_add_planet()
    cis_index.select_planet(data.VENUS_NAME)

    # ✅ ASSERT
    cis_index.verify_text(
        element=cis_index.scan_planet_name, expected_text=data.VENUS_NAME
    )
    cis_index.verify_text(
        element=cis_index.archive_list, expected_text=data.CIS_NO_SCAN_ARCHIVE
    )
    cis_index.verify_text(
        element=cis_index.system_telemetry,
        expected_text=data.GREEN_TELEMETRY_CIS_TARGET_VENUS,
    )
