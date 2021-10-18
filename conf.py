import keyring

query = "RPA impact"
num_page = 2
sender = "mdiendorfer@edu.hse.ru"
password = keyring.get_password("HSE_RS", sender)
receiver = "mdiendorfer@edu.hse.ru"