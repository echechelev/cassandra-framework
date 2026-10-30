import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🌍 Расчет CIS: Земля (Эталон)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_cis_calculation_earth_reference(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету "EARTH".
    4. Нажать на кнопку "ANALYZE CIS" и дождаться окончания сканирования.
    5. Проверить % результата сканирования - 100%.
    6. Проверить результат статуса сканирования - "HIGHLY HABITABLE".
    7. Проверить параметр "HABITABLE ZONE" - 100%.
    8. Проверить параметр "HYDROSPHERE" - 100%.
    9. Проверить параметр "BREATHABILITY" - 100%.
    10. Проверить параметр "GRAVITY" - 100%.
    11. Проверить параметр "STAR RADIATION" - 65%.
    12. Проверить параметр "SURFACE" - 100%.
    13. Проверить параметр "ATMOSPHERE" - 100%.
    14. Проверить параметр "CLIMATE" - 100%.
    15. Проверить параметр "MAGNETIC" - 100%.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.EARTH_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.validate_complete_cis_calculation(
        expected_score="100.0%",
        expected_status="HIGHLY HABITABLE",
        expected_params={
            "HABITABLE ZONE": "100",
            "HYDROSPHERE": "100",
            "BREATHABILITY": "100",
            "GRAVITY": "100",
            "STAR RADIATION": "65",
            "SURFACE": "100",
            "ATMOSPHERE": "100",
            "CLIMATE": "100",
            "MAGNETIC": "100",
        },
    )


@allure.id("CAS-02")
@allure.title("🟢 Расчет CIS зеленая зона")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_cis_calculation_green_zone(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету "TRAPPIST-1E".
    4. Нажать на кнопку "ANALYZE CIS" и дождаться окончания сканирования.
    5. Проверить % результата сканирования - 77.0.
    6. Проверить результат статуса сканирования - "HIGHLY HABITABLE".
    7. Проверить параметр "HABITABLE ZONE" - 85%.
    8. Проверить параметр "HYDROSPHERE" - 80%.
    9. Проверить параметр "BREATHABILITY" - 10%.
    10. Проверить параметр "GRAVITY" - 90%.
    11. Проверить параметр "STAR RADIATION" - 40%.
    12. Проверить параметр "SURFACE" - 95%.
    13. Проверить параметр "ATMOSPHERE" - 70%.
    14. Проверить параметр "CLIMATE" - 60%.
    15. Проверить параметр "MAGNETIC" - 60%.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1E_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.validate_complete_cis_calculation(
        expected_score="77.0%",
        expected_status="HIGHLY HABITABLE",
        expected_params={
            "HABITABLE ZONE": "85",
            "HYDROSPHERE": "80",
            "BREATHABILITY": "10",
            "GRAVITY": "90",
            "STAR RADIATION": "40",
            "SURFACE": "95",
            "ATMOSPHERE": "70",
            "CLIMATE": "60",
            "MAGNETIC": "60",
        },
    )


@allure.id("CAS-03")
@allure.title("🟡 Расчет CIS желтая зона")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_cis_calculation_yellow_zone(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету "TRAPPIST-1F".
    4. Нажать на кнопку "ANALYZE CIS" и дождаться окончания сканирования.
    5. Проверить % результата сканирования - 70.5%.
    6. Проверить результат статуса сканирования - "CONDITIONALLY HABITABLE".
    7. Проверить параметр "HABITABLE ZONE" - 80%.
    8. Проверить параметр "HYDROSPHERE" - 70%.
    9. Проверить параметр "BREATHABILITY" - 5%.
    10. Проверить параметр "GRAVITY" - 95%.
    11. Проверить параметр "STAR RADIATION" - 35%.
    12. Проверить параметр "SURFACE" - 90%.
    13. Проверить параметр "ATMOSPHERE" - 60%.
    14. Проверить параметр "CLIMATE" - 50%.
    15. Проверить параметр "MAGNETIC" - 50%.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1F_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.validate_complete_cis_calculation(
        expected_score="70.5%",
        expected_status="CONDITIONALLY HABITABLE",
        expected_params={
            "HABITABLE ZONE": "80",
            "HYDROSPHERE": "70",
            "BREATHABILITY": "5",
            "GRAVITY": "95",
            "STAR RADIATION": "35",
            "SURFACE": "90",
            "ATMOSPHERE": "60",
            "CLIMATE": "50",
            "MAGNETIC": "50",
        },
    )


@allure.id("CAS-04")
@allure.title("🔴 Расчет CIS красная зона")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_cis_calculation_red_zone(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету "PROXIMA B".
    4. Нажать на кнопку "ANALYZE CIS" и дождаться окончания сканирования.
    5. Проверить % результата сканирования - 50.6%.
    6. Проверить результат статуса сканирования - "MARGINALLY HABITABLE".
    7. Проверить параметр "HABITABLE ZONE" - 75%.
    8. Проверить параметр "HYDROSPHERE" - 40%.
    9. Проверить параметр "BREATHABILITY" - 0%.
    10. Проверить параметр "GRAVITY" - 95%.
    11. Проверить параметр "STAR RADIATION" - 85%.
    12. Проверить параметр "SURFACE" - 100%.
    13. Проверить параметр "ATMOSPHERE" - 30%.
    14. Проверить параметр "CLIMATE" - 35%.
    15. Проверить параметр "MAGNETIC" - 20%.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.PROXIMA_B_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.validate_complete_cis_calculation(
        expected_score="50.6%",
        expected_status="MARGINALLY HABITABLE",
        expected_params={
            "HABITABLE ZONE": "75",
            "HYDROSPHERE": "40",
            "BREATHABILITY": "0",
            "GRAVITY": "95",
            "STAR RADIATION": "85",
            "SURFACE": "100",
            "ATMOSPHERE": "30",
            "CLIMATE": "35",
            "MAGNETIC": "20",
        },
    )


@allure.id("CAS-05")
@allure.title("⚪ Расчет CIS серая зона")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_cis_calculation_gray_zone(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету "MERCURY".
    4. Нажать на кнопку "ANALYZE CIS" и дождаться окончания сканирования.
    5. Проверить % результата сканирования - 19.8%.
    6. Проверить результат статуса сканирования - "UNINHABITABLE".
    7. Проверить параметр "HABITABLE ZONE" - 10%.
    8. Проверить параметр "HYDROSPHERE" - 0%.
    9. Проверить параметр "BREATHABILITY" - 0%.
    10. Проверить параметр "GRAVITY" - 38%.
    11. Проверить параметр "STAR RADIATION" - 100%.
    12. Проверить параметр "SURFACE" - 100%.
    13. Проверить параметр "ATMOSPHERE" - 0%.
    14. Проверить параметр "CLIMATE" - 5%.
    15. Проверить параметр "MAGNETIC" - 5%.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.MERCURY_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.validate_complete_cis_calculation(
        expected_score="19.8%",
        expected_status="UNINHABITABLE",
        expected_params={
            "HABITABLE ZONE": "10",
            "HYDROSPHERE": "0",
            "BREATHABILITY": "0",
            "GRAVITY": "38",
            "STAR RADIATION": "100",
            "SURFACE": "100",
            "ATMOSPHERE": "0",
            "CLIMATE": "5",
            "MAGNETIC": "5",
        },
    )


@allure.id("CAS-06")
@allure.title("🔒 Блокировка интерфейса во время анимации сканирования")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_ui_blocked_during_scan(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету "EPSILON ERIDANI C".
    4. Нажать на кнопку ANALYZE CIS, не дожидаться завершения сканирования.
    5. Проверить: кнопки ADD PLANET, ANALYZE CIS, CLEAR ALL, INDEX INFO - disabled.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.EPSILON_ERIDANI_C_NAME)
    cis_index.click_analyze_cis(wait_for_completion=False)

    # ✅ ASSERT
    cis_index.verify_button_state(cis_index.add_planet_btn, is_enabled=False)
    cis_index.verify_button_state(cis_index.analyze_cis_btn, is_enabled=False)
    cis_index.verify_button_state(cis_index.clear_all_btn, is_enabled=False)
    cis_index.verify_button_state(cis_index.index_info_btn, is_enabled=False)


@allure.id("CAS-07")
@allure.title("🎨 Проверка цветовой кодировки параметров")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_color_coding(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Выбрать планету "TAU CETI H".
    3. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    4. Проверить: параметр "SURFACE" - 🟢 Зеленый (#2ecc71) ➡️ rgb(46, 204, 113).
    5. Проверить: параметр "HABITABLE ZONE" - 🟡 Желтый (#f1c40f) ➡️ rgb(241, 196, 15).
    6. Проверить: параметр "ATMOSPHERE" - 🔴 Красный (#e74c3c) ➡️ rgb(231, 76, 60).
    7. Проверить: параметр "CLIMAT" - ⚪ Серый (#7f8c8d) ➡️ rgb(127, 140, 141).
    8. Проверить: параметр STAR RADIATION - ⚠️ Желто-черный полосатый ➡️ rgb(241, 196, 15).
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.TAU_CETI_H_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.verify_param_bar_color("SURFACE", "rgb(46, 204, 113)")
    cis_index.verify_param_bar_color("HABITABLE ZONE", "rgb(241, 196, 15)")
    cis_index.verify_param_bar_color("ATMOSPHERE", "rgb(231, 76, 60)")
    cis_index.verify_param_bar_color("CLIMATE", "rgb(127, 140, 141)")
    cis_index.verify_param_bar_is_striped("STAR RADIATION", "rgb(241, 196, 15)")


@allure.id("CAS-08")
@allure.title("🗃️ Автоматическая сортировка архива по убыванию CIS")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_archive_sort_by_cis_desc(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "MARS".
    4. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    5. Повторить: пункты с 1-4, добавить планеты "EARTH" и "VENUS"
    6. Проверить: в выдаче архива, планеты соритуются по % в порядке "EARTH", "MARS", "VENUS".
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.VENUS_NAME)
    cis_index.click_analyze_cis()

    cis_index.click_add_planet()
    cis_index.select_planet(data.MARS_NAME)
    cis_index.click_analyze_cis()

    cis_index.click_add_planet()
    cis_index.select_planet(data.EARTH_NAME)
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.verify_archive_sorted_by_score_descending()


@allure.id("CAS-09")
@allure.title("🔄 Восстановление состояния сканера после перезагрузки страницы (F5)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_state_persistence_on_f5(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "MERCURY".
    4. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    5. Нажать на кнопку "F5" обновление страницы.
    6. Проверить: URL.
    7. Проверить: имя планеты в заголовке зоны выдачи.
    8. Проверить: итоговый % CIS.
    9. Проверить: запись в архиве.
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.MERCURY_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_refresh_page()

    # ✅ ASSERT
    cis_index.wait_for_url(data.CIS_INDEX_TABLE_URL)
    cis_index.verify_text(cis_index.scan_planet_name, expected_text=data.MERCURY_NAME)
    cis_index.validate_complete_cis_calculation(expected_score="19.8%")
    cis_index.verify_planet_in_archive(data.MERCURY_NAME)


@allure.id("CAS-10")
@allure.title(
    "⏪ Восстановление состояния сканера после нажатия кнопки 'Назад' в браузере"
)
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_state_persistence_on_back(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "MARS".
    4. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    5. Нажать на кнопку "Назад в браузере".
    6. Нажать на кнопку "CIS INDEX TABLE".
    7. Проверить: URL.
    8. Проверить: имя планеты в заголовке зоны выдачи.
    9. Проверить: итоговый % CIS.
    10. Проверить: запись в архиве.
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.MARS_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_browser_back()
    cis_index.pause(1)
    cis_index.click_cis_index_table()

    # ✅ ASSERT
    cis_index.wait_for_url(data.CIS_INDEX_TABLE_URL)
    cis_index.verify_text(cis_index.scan_planet_name, expected_text=data.MARS_NAME)
    cis_index.validate_complete_cis_calculation(expected_score="44.0%")
    cis_index.verify_planet_in_archive(data.MARS_NAME)


@allure.id("CAS-11")
@allure.title("🧭 Восстановление состояния сканера после перехода на Дашборд и возврат")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_state_persistence_on_nav(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "NEPTUNE".
    4. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    5. Нажать на кнопку "DASHBOARD".
    6. Нажать на кнопку "CIS INDEX TABLE".
    7. Проверить: URL.
    8. Проверить: имя планеты в заголовке зоны выдачи.
    9. Проверить: итоговый % CIS.
    10. Проверить: запись в архиве.
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.NEPTUNE_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_dashboard()
    cis_index.pause(1)
    cis_index.click_cis_index_table()

    # ✅ ASSERT
    cis_index.wait_for_url(data.CIS_INDEX_TABLE_URL)
    cis_index.verify_text(cis_index.scan_planet_name, expected_text=data.NEPTUNE_NAME)
    cis_index.validate_complete_cis_calculation(expected_score="37.3%")
    cis_index.verify_planet_in_archive(data.NEPTUNE_NAME)


@allure.id("CAS-12")
@allure.title("🗑️ Корректная работа кнопки CLEAR ALL")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_archive_clear_all(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "TRAPPIST-1F".
    4. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    5. Нажать кнопку "Add planet".
    6. Выбрать планету "TRAPPIST-1G".
    7. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    8. Нажать на кнопку "Clear All".
    9. Нажать на кнопку "Clear All", в модальном окне.
    10. Проверить: архив очищается, нет записей о сканировании "TRAPPIST-1F" и "TRAPPIST-1G".
    11. Проверить: в зоне архива появляется надпись "NO SCANS IN ARCHIVE".
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1F_NAME)
    cis_index.click_analyze_cis()
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1G_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_clear_all()
    cis_index.click_confirm_delete(clear_all_modal=True)

    # ✅ ASSERT
    cis_index.verify_planet_in_archive(data.TRAPPIST_1F_NAME, should_exist=False)
    cis_index.verify_planet_in_archive(data.TRAPPIST_1G_NAME, should_exist=False)
    cis_index.verify_text(
        element=cis_index.archive_list, expected_text=data.CIS_NO_SCAN_ARCHIVE
    )


@allure.id("CAS-13")
@allure.title("🗑️ Корректная работа кнопки DELETE для одной записи")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.states
def test_archive_delete_single(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать кнопку "Add planet".
    3. Выбрать планету "TRAPPIST-1C".
    4. Нажать на кнопку ANALYZE CIS, дождаться завершения сканирования.
    5. Нажать кнопку "DELETE" в зоне архива. 
    6. Нажать кнопку "DELETE" в модальном окне.
    7. Проверить: архив очищается, нет записи о сканировании "TRAPPIST-1C".
    8. Проверить: в зоне архива появляется надпись "NO SCANS IN ARCHIVE".
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1C_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_delete_for_planet(data.TRAPPIST_1C_NAME)
    cis_index.click_confirm_delete(delete_modal=True)

    # ✅ ASSERT
    cis_index.verify_planet_in_archive(data.TRAPPIST_1C_NAME, should_exist=False)
    cis_index.verify_text(
        element=cis_index.archive_list, expected_text=data.CIS_NO_SCAN_ARCHIVE
    )

