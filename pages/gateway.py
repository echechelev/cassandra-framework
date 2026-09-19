import allure
from selene import be, browser, have
from selene.core.entity import Element
from selenium.common.exceptions import TimeoutException, WebDriverException

from pages.core import CorePage


class GatewayPage(CorePage):
    """Логин, Регистрация и Восстановление."""

    # Наследуемые поля (Переопределяются в дочерних классах)
    callsign_input: Element
    access_code_input: Element
    confirm_access_code_input: Element
    recovery_cipher_input: Element

    # Абстрактные свойства (требуют реализации через @property в дочерних классах)
    @property
    def toggle_password(self) -> Element:
        """Переключатель видимости паролей."""
        raise NotImplementedError("Дочерний класс должен реализовать toggle_password") 

    # ========================================================================
    # region 1️⃣ ⌨️ ЗАПОЛНЕНИЕ ПОЛЕЙ
    # ========================================================================

    @allure.step("Ввод позывного")
    def enter_callsign(self, callsign: str, clear_first: bool = False):
        """Вводит позывной в поле Callsign. Если clear_first=True, сначала очищает поле.

        Args:
            callsign: Позывной.
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(f"Вводим позывной: '{callsign}' (очистка: {clear_first})"):
            try:
                self.callsign_input.should(be.visible)

                if clear_first:
                    self.callsign_input.clear()

                self.callsign_input.type(callsign)

            except TimeoutException:
                raise AssertionError(
                    "❌ Callsign field not found or not visible!\n"
                    f"   Callsign: {callsign}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering callsign!\n"
                    f"   Callsign: {callsign}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Ввод ключа доступа")
    def enter_access_code(self, access_code: str, clear_first: bool = False):
        """Вводит ключ доступа в поле Access Code. Если clear_first=True, сначала очищает поле.

        Args:
            access_code: Ключ доступа.
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(
            f"Вводим ключ доступа: '{access_code}' (очистка: {clear_first})"
        ):
            try:
                self.access_code_input.should(be.visible)

                if clear_first:
                    self.access_code_input.clear()

                self.access_code_input.type(access_code)

            except TimeoutException:
                raise AssertionError(
                    "❌ Access Code field not found or not visible!\n"
                    f"   Access Code: {access_code}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering access code!\n"
                    f"   Access Code: {access_code}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Вводим текст в поле Confirm Access Code")
    def enter_confirm_access_code(self, confirm_code: str, clear_first: bool = False):
        """
        Вводит текст в поле Confirm Access Code.
        Использует .type() для корректного срабатывания JS-события input.

        Args:
            confirm_code: Строка с подтверждением кода доступа (например, '123456').
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(f"Вводим Confirm Access Code: '{confirm_code}' (очистка: {clear_first})"):
            try:
                self.confirm_access_code_input.should(be.visible)

                if clear_first:
                    self.confirm_access_code_input.clear()

                self.confirm_access_code_input.type(confirm_code)
            except TimeoutException:
                raise AssertionError(
                    "❌ Failed to enter Confirm Access Code!\n"
                    f"   Expected input: '{confirm_code}'\n"
                    f"   Element: {self.confirm_access_code_input}\n"
                    "   Timeout: confirm_access_code_input did not appear or was not interactable"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering Confirm Access Code!\n"
                    f"   Expected input: '{confirm_code}'\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Вводим текст в поле Recovery Cipher")
    def enter_recovery_cipher(self, cipher: str, clear_first: bool = False):
        """
        Вводит текст в поле Recovery Cipher.
        Использует .type() для корректного срабатывания JS-события input.

        Args:
            cipher: Строка с шифром восстановления (например, 'ABC-123-XYZ').
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(f"Вводим Recovery Cipher: '{cipher}' (очистка: {clear_first})"):
            try:
                self.recovery_cipher_input.should(be.visible)

                if clear_first:
                    self.recovery_cipher_input.clear()

                self.recovery_cipher_input.type(cipher)
            except TimeoutException:
                raise AssertionError(
                    "❌ Failed to enter Recovery Cipher!\n"
                    f"   Expected input: '{cipher}'\n"
                    f"   Element: {self.recovery_cipher_input}\n"
                    "   Timeout: recovery_cipher_input did not appear or was not interactable"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering Recovery Cipher!\n"
                    f"   Expected input: '{cipher}'\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 2️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

    @allure.step("Клик по кнопке переключения видимости пароля (Глаз)")
    def click_toggle_password(self):
        """Нажимает на иконку глаза, чтобы показать/скрыть пароль."""
        try:
            self.toggle_password.click()
        except Exception as e:
            raise AssertionError(
                f"❌ Failed to click toggle password button!\n" f"   Error: {e}"
            ) from e
        return self

    # endregion

    # ========================================================================
    # region 2️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    @allure.step("Проверяем значение поля")
    def verify_field_value(self, element, expected_value: str):
        """Проверяет, что в поле осталось только ожидаемое значение."""
        try:
            element.should(have.value(expected_value))
        except TimeoutException:
            actual_value = element.get_attribute("value")
            raise AssertionError(
                "❌ Значение поля не совпадает!\n"
                f"   Expected: '{expected_value}'\n"
                f"   Actual: '{actual_value}'"
            )
        return self

    @allure.step("Проверяем значение поля ввода (input)")
    def verify_input_value(self, element, expected_value: str):
        """
        Проверяет, что поле ввода содержит ожидаемое значение.
        Использует have.value() для корректной проверки тегов <input>.

        Args:
            element: Элемент поля ввода (input) для проверки.
            expected_value: Ожидаемое значение поля.
        """
        try:
            element.should(have.value(expected_value))
        except TimeoutException:
            raise AssertionError(
                "❌ Input value mismatch!\n"
                f"   Expected value: '{expected_value}'\n"
                f"   Actual value: '{element.get_attribute('value')}'\n"
                "   Condition: Input field must contain the exact value"
            )
        return self

    @allure.step("Проверка ограничения максимальной длины поля")
    def verify_max_length(self, element, max_length: int, char: str = "A"):
        """Универсальный метод проверки maxlength.

        Args:
            element: Selene-элемент (например, self.callsign_input)
            max_length: Максимально допустимая длина (например, 100)
            char: Символ для заполнения (по умолчанию 'A')
        """
        with allure.step(f"Проверка лимита: {max_length} символов"):
            try:
                element.clear()
                element.type(char * max_length)

                current_value = element().get_attribute("value") or ""

                if len(current_value) != max_length:
                    raise AssertionError(
                        f"❌ Length mismatch before extra char!\n"
                        f"   Expected: {max_length}\n"
                        f"   Actual: {len(current_value)}"
                    )

                try:
                    element.type(char)
                except WebDriverException:
                    pass

                final_value = element().get_attribute("value") or ""
                if len(final_value) != max_length:
                    raise AssertionError(
                        f"❌ Max length limit failed! Extra character was added.\n"
                        f"   Expected: {max_length}\n"
                        f"   Actual: {len(final_value)}"
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying max length!\n"
                    f"   Max length: {max_length}\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step(
        "Проверяем состояние поля: пустое и (только для чтения / редактируемое)"
    )
    def verify_empty_field_state(self, element, is_readonly: bool = True):
        """
        Проверяет, что поле ввода пустое и имеет (или не имеет) атрибут readonly.

        Args:
            element: Элемент поля ввода (input) для проверки.
            is_readonly: Если True — проверяет наличие атрибута readonly (заблокировано).
                         Если False — проверяет отсутствие атрибута readonly (доступно для ввода).
        """

        try:
            element.should(have.value(""))
        except TimeoutException:
            raise AssertionError(
                "❌ Field is not empty!\n"
                f"   Expected value: ''\n"
                f"   Actual value: '{element.get_attribute('value')}'\n"
                "   Condition: Field must be empty"
            )

        state_desc = (
            "readonly (заблокировано)"
            if is_readonly
            else "editable (доступно для ввода)"
        )

        try:
            if is_readonly:
                element.should(have.attribute("readonly"))
            else:
                element.should(have.no.attribute("readonly"))
        except TimeoutException:
            actual_readonly_val = element.get_attribute("readonly")
            raise AssertionError(
                f"❌ Field is not {state_desc}!\n"
                f"   Expected: attribute 'readonly' to be {'present' if is_readonly else 'absent'}\n"
                f"   Actual readonly attribute value: '{actual_readonly_val}'\n"
                "   Condition: Field readonly state mismatch"
            )

    @allure.step("Проверка появления контейнера ошибки")
    def should_show_error_container(self, element: Element, expected_text: str):
        """Проверяет, что контейнер ошибки отображается и содержит верный текст.

        Args:
            element: Selene-элемент (контейнер ошибки)
            expected_text: точный текст для проверки
        """
        with allure.step(f"Ожидаемый текст ошибки: '{expected_text}'"):
            try:
                element.should(be.visible).should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    "❌ Контейнер ошибки не отображается или текст не совпадает!\n"
                    f"   Expected text: '{expected_text}'\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking error container!\n"
                    f"   Expected text: '{expected_text}'\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверяем состояние кнопки")
    def verify_button_state(self, element, is_disabled: bool = True):
        """
        Проверяет состояние кнопки (активна или неактивна).

        Args:
            element: Элемент кнопки (button) для проверки.А
            is_disabled: Ожидаемое состояние. True - неактивна (disabled), False - активна (enabled).
        """
        try:
            if is_disabled:
                element.should(be.disabled)
            else:
                element.should(be.enabled)
        except TimeoutException:
            expected_state = "DISABLED" if is_disabled else "ENABLED"
            actual_state = (
                "DISABLED" if element.get_attribute("disabled") else "ENABLED"
            )

            raise AssertionError(
                f"❌ Button state mismatch!\n"
                f"   Expected state: {expected_state}\n"
                f"   Actual state: {actual_state}\n"
                f"   Element: {element}"
            )

        return self

    # endregion
