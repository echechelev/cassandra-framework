import allure
import pytest
from selene import be, browser

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
    cis_index.add_and_scan_planets([data.TEEGARDEN_C_NAME, data.TEEGARDEN_B_NAME])

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
@allure.title("⏹️ Сценарий отмены сканирования и сброса")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.workflows
def test_cancel_scan_and_reset(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "MERCURY".
    4. Нажать кнопку "Add planet".
    5. Выбрать планету "VENUS".
    6. Проверить имя планеты в заголовке зоны сканирования - VENUS.
    7. Проверить: зона выдачи в архиве содержит запись "NO SCANS IN ARCHIVE".
    8. Проверить текст телеметрии - "TARGET ACQUIRED: VENUS. DATA LOADED. READY FOR SCAN.".
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


@allure.id("CAS-03")
@allure.title("🔄 Повторное сканирование планеты после её удаления из архива")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.workflows
def test_rescanning_after_archive_removal(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "MARS".
    4. Нажать кнопку "ANALYZE CIS" и дождаться завершения анимации сканирования.
    5. Нажать на кнопку "DELETE" в архиве на записи "MARS".
    6. Нажать на кнопку "DELETE" в модалке удаления.
    7. Проверить: запись "MARS" удалилась из архива.
    8. Проверить: зона сканера имеет текст "DEEP SCAN TERMINAL READY".
    9. Проверить: зона архива имеет текст "NO SCANS IN ARCHIVE".
    10. Проверить: кнопка "ANALYZE CIS" заблокирована - "DISABLED".
    11. Повторить: шаги 1-4, снова добавить и отсканировать планету "MARS".
    12. Проверить: запись добавлена в архив.
    13. Проверить: кнопка "ANALYZE CIS" заблокирована - "DISABLED".
    """

    # 🎬 ARRANGE
    cis_index.add_and_scan_planets([data.MARS_NAME])

    # ⚡ ACT
    cis_index.click_delete_for_planet(data.MARS_NAME)
    cis_index.click_confirm_delete(delete_modal=True)
    cis_index.wait_for_data_sync(1)

    # ✅ ASSERT
    cis_index.verify_planet_in_archive(data.MARS_NAME, should_exist=False)
    cis_index.verify_text(
        cis_index.scanner_empty, expected_text=data.CIS_TEXT_DEEP_SCAN_READY
    )
    cis_index.verify_text(
        cis_index.archive_list, expected_text=data.CIS_NO_SCAN_ARCHIVE
    )
    cis_index.verify_button_state(cis_index.analyze_cis_btn, is_enabled=False)

    # ⚡ ACT
    cis_index.add_and_scan_planets([data.MARS_NAME])

    # ✅ ASSERT
    cis_index.verify_planet_in_archive(data.MARS_NAME)
    cis_index.verify_button_state(cis_index.analyze_cis_btn, is_enabled=False)


@allure.id("CAS-04")
@allure.title("ℹ️ Проверка доступности кнопки INDEX INFO в разных состояниях")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.workflows
def test_index_info_button_state_verification(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Проверить: кнопка "INDEX INFO" активна - enabled.
    3. Нажать кнопку "Add planet".
    4. Выбрать планету "URANUS".
    5. Нажать кнопку "ANALYZE CIS" и не дождаться завершения сканирования.
    6. Проверить: кнопка "INDEX INFO" во время сканирования неактивна - DESABLED.
    7. Проверить: после сканирования кнопка "INDEX INFO" - "ENABLED".
    """

    # ✅ ASSERT
    cis_index.verify_button_state(cis_index.index_info_btn, is_enabled=True)

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.URANUS_NAME)
    cis_index.click_analyze_cis(wait_for_completion=False)

    # ✅ ASSERT
    cis_index.verify_button_state(cis_index.index_info_btn, is_enabled=False)

    # ⏳ Ожидание завершения анимации (временно увеличиваем таймаут)
    old_timeout = browser.config.timeout
    browser.config.timeout = 12

    try:
        cis_index.cis_result.should(be.visible)
    finally:
        browser.config.timeout = old_timeout

    # ✅ ASSERT
    cis_index.verify_button_state(cis_index.index_info_btn, is_enabled=True)
