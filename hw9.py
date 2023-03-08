contacts = {}


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError as e:
            return f"{e.args[0]} not found in contacts."

        except ValueError:
            return 'Give me name and phone please.'

        except IndexError:
            return 'Enter user name'

    return inner


def handle_hello():
    return 'How can I help you?'


@input_error
def handle_add(contact, phone_number):
    contacts[contact] = phone_number
    return f' {contact.title()}, your phone number has been added as {phone_number}.'


@input_error
def handle_change_phone(contact, phone_number):
    if contact not in contacts:
        return f' A contact {contact} is not found.'
    else:
        contacts[contact] = phone_number
        return f'{contact}, your phone number has been updated to {phone_number}'


@input_error
def handle_show_phone(contact):
    if contact not in contacts:
        return f'A contact {contact} is not found'
    else:
        return f'The phone number for {contact} is {contacts[contact]}.'


@input_error
def handle_show_all():
    if not contacts:
        return 'There are no contacts saved.'
    contacts_string = ""
    for contact, phone in contacts.items():
        contacts_string += f'{contact}: {phone}\n'
    return contacts_string


def handle_bye():
    return 'Good bye!'


handlers = {
    'hello': handle_hello,
    'add': handle_add,
    'change': handle_change_phone,
    'phone': handle_show_phone,
    'show all': handle_show_all,
    'good bye': handle_bye,
    'close': handle_bye,
    'exit': handle_bye,
    '.': handle_bye
}


def command_parser(user_command):
    for command_name, command in handlers.items():
        if user_command.startswith(command_name):
            return command, user_command.replace(command_name, '').strip().split()
    return None,  None


def main():
    while True:
        # add iryna 0673957362
        user_input = input('Enter your command: ').lower()
        command, contact_data = command_parser(user_input)
        if command:
            print(command(*contact_data))
        if user_input in ['.', 'good bye', 'close', 'exit']:
            break
        else:
            print('Such command does not exist. Enter anoter command.')


if __name__ == '__main__':
    main()
