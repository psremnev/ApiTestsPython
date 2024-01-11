def open_page(driver, page_address):
    driver.get(page_address)
    driver.maximize_window()


def get_error_message(message, current, test):
    return f'{message and "."}\n Текущий: {current}. Ожидаемый: {test}/n'
