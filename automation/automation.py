import re

def main(filename):
    # Variables
    input_text = ''
    input_list = []
    potential_phone_numbers = []
    potential_emails = []
    good_phone_numbers = []
    good_emails = []

    # Read txt file into template
    input_text = read_template(filename)

    # Parse text into list of words separated by spaces
    input_list = input_text.split()

    # Divide list into potential emails / phone numbers
    for word in input_list:
        # If word has @, pop from input_list, push to potential emails
        # Else: if word has at least 7 numbers, push to potential phone number list
        if '@' in word:
            potential_emails.append(word)
        else:
            if sum(char.isdigit() for char in word) > 6:
                potential_phone_numbers.append(word)

    # validate contacts
    good_emails = validate_email(potential_emails)
    good_phone_numbers = validate_phone(potential_phone_numbers)

    # Remove duplicates
    good_emails = remove_duplicates(good_emails)
    good_phone_numbers = remove_duplicates(good_phone_numbers)

    # Sort
    good_emails.sort()
    good_phone_numbers.sort()

    # Add results to text file
    save_to_file(good_emails, './automation/assets/email-contacts.txt')
    save_to_file(good_phone_numbers, './automation/assets/phone-contacts.txt')

def read_template(filename):
    try:
        with open(filename, "r") as template_file:
            template_content = template_file.read()
            template_content = template_content.strip()
            return template_content
    except FileNotFoundError:
        raise FileNotFoundError

def validate_email(potential_emails):
    good_emails = []
    bad_emails = [] # for testing purposes only

    for address in potential_emails:
        valid_email = True
        bad_characters = '(),:"";<>[\]'

        # 1 and only @ exists
        sum_of_at = 0
        for char in address:
            if char == '@':
                sum_of_at += 1
        if sum_of_at != 1:
            valid_email = False
            bad_emails.append(address)

        # entire length: 254 characters
        elif len(address) > 254:
            valid_email = False
            bad_emails.append(address)

        # check for bad characters
        else:
            for char in address:
                if char in bad_characters:
                    valid_email = False
                    bad_emails.append(address)

        # Check local / domain parts of email
        if valid_email is True:
            local, domain = address.split("@")

            # Check local part
            if len(local) > 64:
                valid_email = False
                bad_emails.append(address)

            elif local[0] == '.':
                valid_email = False
                bad_emails.append(address)

            elif local[-1] == '.':
                valid_email = False
                bad_emails.append(address)

        # Passes all test - add to list
        if valid_email is True:
            good_emails.append(address)

    return good_emails

def validate_phone(input_phone_num):
    good_phone_num = []
    bad_phone_num = [] # for testing purposes only


    for phone_num in input_phone_num:
        num_to_test = phone_num
        valid_number = True

        # split word by x into extension and main
        if 'x' in num_to_test:
            main, extension = num_to_test.split('x')
        else:
            main = num_to_test
            extension = ''

        # Format extension
        extension = re.sub("[^0-9]", "", extension)
        if len(extension) != 0:
            extension = 'x' + extension

        # Format main
        main = re.sub("[^0-9]", "", main)

        # keep items if main length is 7 or 10
        if not(len(main) == 7 or len(main) == 10):
            valid_number = False
            bad_phone_num.append(phone_num)

        # if 7 digits, add 206 area code
        if len(main) == 7:
            print(main)
            main = f'206-{main[0:3]}-{main[3:7]}'

        # 10 digits
        elif len(main) == 10:
            main = f'{main[0:3]}-{main[3:6]}-{main[6:10]}'

        # Check for valid area code
        if len(main) > 0:
            if main[0] == '0' or main[0] == '1':
                valid_number = False
                bad_phone_num.append(phone_num)

        # Passes all tests - add to good phone number list
        if valid_number is True:
            good_phone_num.append(f'{main}{extension}')

    return good_phone_num

def remove_duplicates(input_list):
    temp_list = []
    for item in input_list:
        if item not in temp_list:
            temp_list.append(item)
    return temp_list

def save_to_file(list, filename):
    with open(filename, 'w+') as f:
        for word in list:
            f.write(f'{word}\n')

if __name__ == "__main__":
    main('./automation/assets/potential-contacts.txt')