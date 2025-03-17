def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args