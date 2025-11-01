def input_number_handling(input_message):
    while True:
        try:
            user_input = int(input(input_message))
            return user_input
        except ValueError:
            print("Mohon Masukan Angka!\n")
            continue

def input_handling(input_message):
    while True:

        try:
            user_input = input(input_message)
            if user_input == "" or user_input == " "*len(user_input):
                raise ValueError("Input tidak boleh kosong, silahkan coba lagi!\n")
            else:
                return user_input
        except ValueError as e:
            print(e)
            continue
