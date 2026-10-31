import allure
import pytest

from pages.cis_index_table import CisIndexTablePage
from tests import data


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.errors_ui
def test_access_denied_redirect_on_empty_storage():
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Проверить: текст телеметрии становится красным и содержит '> ACCESS DENIED. REDIRECTING...'
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'login.html'.
    """

    # ⚡ ACT
    cis_index_table = CisIndexTablePage()
    cis_index_table.open_unauthenticated(data.CIS_INDEX_TABLE_URL)

    # ✅ ASSERT
    cis_index_table.verify_telemetry_text(data.RED_TELEMETRY_ACCESS_DENIED)
    cis_index_table.verify_telemetry_color_with_cassandra(red=True)
    cis_index_table.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-02")
@allure.title("🚫 Попытка запуска сканирования без выбранной планеты")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.errors_ui
def test_attempt_to_scan_without_selected_planet(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Попытаться кликнуть на кнопку "Analyze cis".
    2. Проверить: текст в таблице сканера равен 'DEEP SCAN TERMINAL READY'
    3. Проверить: кнопка неактивна, имеет атрибут 'disabled'.
    """

    # ⚡ ACT
    cis_index.try_click_disabled_button(cis_index.analyze_cis_btn)

    # ✅ ASSERT
    cis_index.verify_text(
        cis_index.scanner_empty, expected_text=data.CIS_TEXT_DEEP_SCAN_READY
    )


@allure.id("CAS-03")
@allure.title("⚠️ Попытка добавления дубликата планеты в архив")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.errors_ui
def test_attempt_to_add_duplicate_planet_to_archive(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Нажать на кнопку "Add planet" и выбрать планету 'Earth'.
    3. Нажать на кнопку "Analyze cis".
    4. Проверить: планета 'Earth', добавлена в архив.
    5. Нажать на кнопку "Add planet" и снова выбрать планету 'Earth'.
    6. Проверить: текст тоста "Scan result for EARTH already in archive. Please select another planet."
    """

    # ⚡ ACT
    cis_index.add_and_scan_planets([data.EARTH_NAME])

    # ✅ ASSERT
    cis_index.verify_planet_in_archive(data.EARTH_NAME)

    # ⚡ ACT
    cis_index.click_add_planet()
    cis_index.select_planet(data.EARTH_NAME, wait_for_close=False)

    # ✅ ASSERT
    cis_index.verify_text(
        cis_index.toast_message, expected_text=data.CIS_ERROR_RESULT_IN_ARCHIVE
    )


@allure.id("CAS-04")
@allure.title("⚠️ Попытка очистки пустого архива")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "cis-index-table")
@pytest.mark.regress
@pytest.mark.cis_index_table
@pytest.mark.errors_ui
def test_attempt_to_clear_an_empty_scan_archive(cis_index):
    """
    Сценарий:
    1. Перейти на страницу 'Cis index table page'.
    2. Попытаться нажать на кнопку "Claear all".
    3. Проверить: кнопка неактивна, имеет атрибут 'disabled'.
    4. Проверить: модальное окно подтверждения удаления не открывается.
    """

    # ⚡ ACT
    cis_index.try_click_disabled_button(cis_index.clear_all_btn)

    # ✅ ASSERT
    cis_index.verify_window_state(cis_index.confirm_delete_modal, is_visible=False)
