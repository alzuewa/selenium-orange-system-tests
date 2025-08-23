from enum import StrEnum

from base_ui.element import By, Element


class Tabs(StrEnum):
    USER_MANAGEMENT_TAB = 'User Management'
    JOB_TAB = 'Job'
    ORGANIZATION_TAB = 'Organization'
    QUALIFICATIONS_TAB = 'Qualifications'
    CORPORATE_BRANDING_TAB = 'Corporate Branding'
    CONFIGURATION_TAB = 'Configuration'


class AdminPageLocators:
    ADD_USER_BUTTON = Element(By.XPATH, '//button//*[contains(@class, "bi-plus")]', 'Add new user button')

    TABS = {
        Tabs.USER_MANAGEMENT_TAB: Element(By.XPATH, '//span[contains(text(), "User Management")]',
                                          'User Management Tab'),
        Tabs.JOB_TAB: Element(By.XPATH, '//span[contains(text(), "Job")]', 'Job Tab'),
        Tabs.ORGANIZATION_TAB: Element(By.XPATH, '//span[contains(text(), "Organization")]', 'Organization Tab'),
        Tabs.QUALIFICATIONS_TAB: Element(By.XPATH, '//span[contains(text(), "Qualifications")]', 'Qualifications Tab'),
        Tabs.CORPORATE_BRANDING_TAB: Element(By.XPATH, '//li//*[contains(text(), "Corporate Branding")]',
                                             'Corporate Branding Tab'),
        Tabs.CONFIGURATION_TAB: Element(By.XPATH, '//span[contains(text(), "Configuration")]', 'Configuration Tab')
    }

    class NewUserLocators:
        CANCEL_BUTTON = Element(By.XPATH, '//*[@class="oxd-form-actions"]//button[text()=" Cancel "]', 'Cancel button')
        SAVE_BUTTON = Element(By.XPATH, '//*[@class="oxd-form-actions"]//*[@type="submit"]', 'Submit button')
