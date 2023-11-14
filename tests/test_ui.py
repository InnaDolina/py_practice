import pytest
import re

from playwright.sync_api import Page, expect


@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):
    # Arrange
    page.goto("https://demo.applitools.com/")

    # Act
    page.locator("#username").fill("User1")
    page.locator("#password").fill("i>12dFt")
    page.locator("#log-in").click()

    # Assert
    expect(page.locator("div.logo-w")).to_be_visible()
    expect(page.locator("#time")).to_be_visible()
    expect(page.get_by_text("Add Account")).to_be_visible()
    expect(page.get_by_text("Make Payment")).to_be_visible()

