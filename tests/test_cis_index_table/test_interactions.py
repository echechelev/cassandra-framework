import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🪐 Открытие модального окна выбора планеты")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_verify_planet_selector_modal_opens_correctly(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Проверить: открылось модальное окно с текстом заголовка 'SELECT SCAN TARGET'
    4. Проверить: в списке видна хотя бы 1 планете в каждой звезде.
    """

    # ⚡ ACT
    cis_index.click_add_planet()

    # ✅ ASSERT
    cis_index.verify_text(
        cis_index.planet_selector_modal,
        expected_text=data.CIS_PLANET_MODAL_TEXT,
    )
    cis_index.verify_planet_visible_in_modal(data.EPSILON_ERIDANI_C_NAME)
    cis_index.verify_planet_visible_in_modal(data.TEEGARDEN_B_NAME)
    cis_index.verify_planet_visible_in_modal(data.PROXIMA_B_NAME)
    cis_index.verify_planet_visible_in_modal(data.TAU_CETI_E_NAME)
    cis_index.verify_planet_visible_in_modal(data.MERCURY_NAME)
    cis_index.verify_planet_visible_in_modal(data.TRAPPIST_1B_NAME)


@allure.id("CAS-02")
@allure.title("🪐 Успешный выбор планеты и переход зоны сканера в активное состояние")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_select_planet_and_activate_scanner(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету 'Mars'
    4. Проверить: окно сканера перешло в активное состояние и отображается.
    5. Проверить: неактивное окно сканера не отображается.
    6. Проверить: название выбранной планеты появляется в зоне сканера.
    7. Проверить: кнопка 'Analyze cis' становитсся активной.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.MARS_NAME)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.scanner_empty, is_visible=False)
    cis_index.verify_window_state(cis_index.scanner_active, is_visible=True)
    cis_index.verify_text(cis_index.scan_planet_name, expected_text=data.MARS_NAME)
    cis_index.verify_button_state(cis_index.analyze_cis_btn, is_enabled=True)


@allure.id("CAS-03")
@allure.title("📋 Открытие и проверка содержимого модального окна INDEX INFO")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_open_and_verify_index_info_modal(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Index info'.
    3. Проверить: заголовок модального окна, содержит текст "CIS SCAN PARAMETERS".
    4. Проверить: отображается параметр "HABITABLE ZONE".
    5. Проверить: отображается параметр "CLIMATE".
    6. Проверить: отображается параметр "STAR RADIATION".
    """

    # ⚡ ACT
    cis_index.click_index_info()

    # ✅ ASSERT
    cis_index.verify_text(
        cis_index.scan_info_modal, expected_text=data.CIS_INFO_MODAL_TEXT
    )
    cis_index.verify_text(
        cis_index.scan_info_modal, expected_text=data.CIS_INFO_MODAL_HABITABLE_ZONE
    )
    cis_index.verify_text(
        cis_index.scan_info_modal, expected_text=data.CIS_INFO_MODAL_CLIMATE
    )
    cis_index.verify_text(
        cis_index.scan_info_modal, expected_text=data.CIS_INFO_MODAL_STAR_RADIATION
    )


@allure.id("CAS-04")
@allure.title("❌ Закрытие модалки 'Добавление планеты'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_сlose_add_planet_modal_via_all_triggers(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. В модалке "Добавление планеты", нажать на кнопку "Close"
    4. Проверить: модалка "Добавление планеты", закрылась.
    5. Нажать на кнопку 'Add planet'.
    6. В модалке "Добавление планеты", нажать на кнопку "Cancel"
    7. Проверить: модалка "Добавление планеты", закрылась.
    """

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.close_add_planet_modal(click_cross=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.planet_selector_modal, is_visible=False)

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.close_add_planet_modal(click_cancel=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.planet_selector_modal, is_visible=False)


@allure.id("CAS-05")
@allure.title("❌ Закрытие модалки 'Индекс инфо'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_сlose_index_info_modal_via_all_triggers(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Index info'.
    3. В модалке "Информация параметров", нажать на кнопку "Close"
    4. Проверить: модалка "Информация параметров", закрылась.
    5. Нажать на кнопку 'Index info'.
    6. В модалке "Информация параметров", нажать на кнопку "Cancel"
    7. Проверить: модалка "Информация параметров", закрылась.
    """

    # ⚡ ACT
    cis_index.click_index_info()
    cis_index.close_index_info_modal(click_cross=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.scan_info_modal, is_visible=False)

    # ⚡ ACT
    cis_index.click_index_info()
    cis_index.close_index_info_modal(click_cancel=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.scan_info_modal, is_visible=False)


@allure.id("CAS-06")
@allure.title("❌ Закрытие модалки 'Подтверждения удаления'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_сlose_confirm_delete_modal_via_all_triggers(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. В модалке "Добавления планеты", выбрать планету 'Mars'
    4. Нажать на кнопку "Analyze cis" и дождаться результатов сканирования.
    5. Нажать на кнопку "Clear all".
    6. В модалке "Подтверждение удаления", нажать на кнопку "Close".
    7. Проверить: модалка "Подтверждение удаления", закрылась.
    8. Нажать на кнопку "Clear all".
    9. В модалке "Подтверждение удаления", нажать на кнопку "Cancel"
    10. Проверить: модалка "Подтверждение удаления", закрылась.
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.MARS_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_clear_all()
    cis_index.close_delete_confirmation_modal(click_cross=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.delete_confirm_clear_all_modal, is_visible=False)

    # ⚡ ACT
    cis_index.click_clear_all()
    cis_index.close_delete_confirmation_modal(click_cancel=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.delete_confirm_clear_all_modal, is_visible=False)


@allure.id("CAS-07")
@allure.title("❌ Закрытие модалки 'Детали'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_сlose_details_modal_via_all_triggers(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. В модалке "Добавления планеты", выбрать планету 'Tau Ceti F'
    4. Нажать на кнопку "Analyze cis" и дождаться результатов сканирования.
    5. Нажать на кнопку "Details", в зоне добавленной архивной записи сканирования Tau ceti F.
    6. В модалке "Детали", нажать на кнопку "Close".
    7. Проверить: модалка "Детали", закрылась.
    8. Нажать на кнопку "Clear all".
    9. В модалке "Детали", нажать на кнопку "Cancel"
    10. Проверить: модалка "Детали", закрылась.
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.TAU_CETI_F_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_details_for_planet(data.TAU_CETI_F_NAME)
    cis_index.close_details_modal(click_cross=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.details_modal, is_visible=False)

    # ⚡ ACT
    cis_index.click_details_for_planet(data.TAU_CETI_F_NAME)
    cis_index.close_details_modal(click_cancel=True)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.details_modal, is_visible=False)


@allure.id("CAS-08")
@allure.title("📂 Проверка открытия деталей (Details) из архива")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_open_planet_details_from_archive(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету 'Venus'
    4. Нажать на кнопку "Analyze cis" и дождаться результатов сканирования.
    5. Нажать на кнопку "Details", в зоне добавленной архивной записи сканирования Venus.  .
    7. Проверить: заголовок модалки содержит имя планеты "Venus".
    8. Проверить: поле "description" содержит описание 'Planet is unsuitable for colonization.'.
    9. Проверить: поле "warning" содержит описание 'CRITICAL: Zero magnetic shielding leaves surface'.
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.VENUS_NAME)
    cis_index.click_analyze_cis()

    # ⚡ ACT
    cis_index.click_details_for_planet(data.VENUS_NAME)

    # ✅ ASSERT
    cis_index.verify_text(cis_index.details_planet_name, expected_text=data.VENUS_NAME)
    cis_index.verify_text(
        cis_index.details_description, expected_text=data.VENUS_CIS_DESCRIPTION
    )
    cis_index.verify_text(
        cis_index.details_warning, expected_text=data.VENUS_CIS_WARNING
    )


@allure.id("CAS-09")
@allure.title("📡 Проверка обновления строки телеметрии во время сканирования")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_verify_telemetry_updates_during_scanning_process(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Проверить: текст телеметрии "> CASSANDRA: SYSTEM READY. ADD TARGET TO BEGIN.".
    3. Нажать на кнопку 'Add planet'.
    4. Выбрать планету 'TRAPPIST-1H'.
    5. Проверить: текст телеметрии "> CASSANDRA: TARGET ACQUIRED: TRAPPIST-1H . DATA LOADED. READY FOR SCAN.".
    6. Нажать на кнопку "Analyze cis" и дождаться результатов сканирования.
    7. Проверить: текст телеметрии "> CASSANDRA: SCAN COMPLETE: TRAPPIST-1H  — CIS 43.0%".
    """

    # ✅ ASSERT
    cis_index.verify_text(
        element=cis_index.system_telemetry,
        expected_text=data.GREEN_TELEMETRY_CIS_READY_TO_BEGIN,
    )

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1H_NAME)

    # ✅ ASSERT
    cis_index.verify_text(
        element=cis_index.system_telemetry,
        expected_text=data.GREEN_TELEMETRY_CIS_TARGET_TRAPPIST_1H,
    )

    # ⚡ ACT
    cis_index.click_analyze_cis()

    # ✅ ASSERT
    cis_index.verify_text(
        element=cis_index.system_telemetry,
        expected_text=data.GREEN_TELEMETRY_CIS_SCAN_COMPLETE_TRAPPIST_1H,
    )


@allure.id("CAS-10")
@allure.title("📡 Проверка обновления строки телеметрии после удаления")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.interactions
def test_verify_telemetry_updates_after_deletion_process(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку 'Add planet'.
    3. Выбрать планету 'TRAPPIST-1H'.
    4. Нажать на кнопку "Analyze cis" и дождаться результатов сканирования.
    5. Нажать на кнопку "Clear all".
    6. В модальном окне "Подтверждения удаления", нажать на кнопку "Clear all".
    7. Проверить: текст телеметрии "> CASSANDRA: ARCHIVE CLEARED. SYSTEM READY.".
    8. Нажать на кнопку 'Add planet'.
    9. Выбрать планету 'TRAPPIST-1H'.
    10. Нажать на кнопку "Analyze cis" и дождаться результатов сканирования.
    11. Нажать на кнопку "DELETE" в зоне добавленной архивной записи сканирования TRAPPIST-1H.
    12. В модальном окне "Подтверждение удаления", нажать на кнопку "DELETE".
    13. Проверить: текст телеметрии "> CASSANDRA: RECORD DELETED: TRAPPIST-1H".
    """

    # 🎬 ARRANGE
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1H_NAME)
    cis_index.click_analyze_cis()
    cis_index.click_clear_all()

    # ⚡ ACT
    cis_index.click_confirm_delete(clear_all_modal=True)

    # ✅ ASSERT
    cis_index.verify_text(
        element=cis_index.system_telemetry,
        expected_text=data.GREEN_TELEMETRY_CIS_ARCHIVE_CLEARED,
    )

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.TRAPPIST_1H_NAME)
    cis_index.click_analyze_cis()
    cis_index.click_delete_for_planet(data.TRAPPIST_1H_NAME)
    cis_index.click_confirm_delete(delete_modal=True)

    # ✅ ASSERT
    cis_index.verify_text(
        element=cis_index.system_telemetry,
        expected_text=data.GREEN_TELEMETRY_CIS_SCAN_RECORD_DELETED_TRAPPIST_1H,
    )
