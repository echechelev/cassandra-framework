import allure
import pytest

from . import data


@allure.id("CAS-05")
@allure.title("📡 Полная последовательность активации 'Uplink'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.uplink
def test_full_uplink_activation_sequence(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    2. Проверяем: кнопка 'Uplink Button', становится неактивной, серой, теряет пульсацию.
    3. Проверяем: кнопка 'Logout' и 5 центральных, приобретают класс 'panel-online', кликабельные,
    яркие с неоновым счечением.
    4. Проверяем: 'Role Panel' и 'User Panel' переключаются в 'panel-online'.
    4. Проверяем: Текст 'Telemetry' становится зеленым и содержит фразу 'SYSTEM READY FOR WORK'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.NAME_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_uplink_button_disabled()
    dashboard_page_aurora.verify_uplink_buttons_activated()
    dashboard_page_aurora.verify_telemetry_color_with_cassandra(green=True)
    dashboard_page_aurora.verify_telemetry_text(
        expected_text=data.TELEMETRY_SYSTEM_READY_AURORA
    )


@allure.id("CAS-06")
@allure.title("🚫 Проверка неактивности кнопки `Logout` до полной активации")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.uplink
def test_logout_button_inactive_before_activation(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'.
    2. Дождидаемcя появления кнопки 'Logout'.
    3. Проверяем: пытаемся кликнуть на кнопку и проверяем url.
    4. Проверяем: кнопкf имеет `CSS` свойство `pointer-events`.
    5. Проверяем: что после клика url не изменился.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ✅ ASSERT
    dashboard_page_aurora.verify_logout_button_inactive()


@allure.id("CAS-07")
@allure.title("🚫 Проверка неактивности кнопок 'Planet Bar' до полной активации")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.uplink
def test_planet_bar_buttons_inactive_before_activation(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'.
    2. Дождидаемcя поочередного появление кнопок 'Planet Bar'.
    3. Проверяем: пытаемся кликнуть на каждую кнопку и проверяем url.
    4. Проверяем: кнопки имеет `CSS` свойство `pointer-events`.
    5. Проверяем: что после каждого клика url не изменился.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ✅ ASSERT
    dashboard_page_aurora.verify_planet_bar_buttons_inactive()


@allure.id("CAS-08")
@allure.title("📊 Валидация анимации и значений прогресс-бара.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.uplink
def test_progress_bar_animation_and_values(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'.
    2. Проверяем: через явные ожидания значение атрибута 'style' у 'Progress Fill',
    значение ширины монотонно возрастает ('10%' -> '22%' -> ... -> '100%') .
    3. Проверяем: через явные ожидания значение атрибута `style` у 'Progress Text',
    текстовое значение синхронизировано с шириной.
    4. Проверяем: в конце контейнер прогресс-бара имеет 'display' 'none' или 'opacity: 0'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.NAME_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_progress_bar_animation()


@allure.id("CAS-09")
@allure.title("💤 Визуальное угасание кнопки 'Uplink' после 100% загрузки")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.uplink
def test_uplink_button_visual_fade_out_after_100_load(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    2. Проверяем: у кнопки 'Uplink Button' отсуствует класс `uplink-active`.
    3. Проверяем: свойство `opacity` равно 0.4.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.NAME_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_uplink_button_disabled()


@allure.id("CAS-10")
@allure.title("🛡️ Защита от спама кликов по кнопке `Uplink`.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.uplink
def test_uplink_spam_click_protection(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполняем 3 клика.`element.click` по кнопке `Uplink` в цикле.
    2. Проверяем: проходит только 1 клик, кнопка становится неактивной.
    3. Проверяем что контейнер 'прогресс-бар', только один.
    """
    # ⚡ ACT
    dashboard_page_aurora.spam_click_diagnostics()

    # ✅ ASSERT
    dashboard_page_aurora.verify_progress_bar_appeared_once()
    dashboard_page_aurora.verify_uplink_button_disabled()
