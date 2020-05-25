import cmd
import seven_up_user
import seven_up_game

gSevenUp = None

# ********************************************************
# CLASS: SevenUp
# ********************************************************
class SevenUp(cmd.Cmd):

    # ********************************************************
    # METHOD: initialize
    # ********************************************************
    def initialize(self):
        print('SevenUp::initialize()')
        self.update_prompt()
        self.users = {}
        self.dealer = ''
        self.game = None

    # ********************************************************
    # METHOD: shutdown
    # ********************************************************
    def shutdown(self):
        print('SevenUp::shutdown()')

    # ********************************************************
    # METHOD: update_prompt
    # ********************************************************
    def update_prompt(self):
        self.prompt = '> '

    # ********************************************************
    # METHOD: new_game
    # ********************************************************
    def new_game(self, num_cards):
        self.game = seven_up_game.Game(num_cards, self.users)

    # ********************************************************
    # METHOD: clear_users
    # ********************************************************
    def clear_users(self):
        self.users = {}

    # ********************************************************
    # COMMANDS
    # ********************************************************

    # ********************************************************
    # COMMAND: new_user
    # ********************************************************
    def do_new_user(self, name):
        print('NEW USER: ' + str(name))
        index = len(self.users)
        self.users[index] = seven_up_user.User()
        self.users[index].initialize(name)

    # ********************************************************
    # COMMAND: example
    # ********************************************************
    def do_example(self, line):
        self.clear_users()
        self.do_new_user('Doug')
        self.do_new_user('Rachel')
        self.do_new_user('Frank')
        self.do_new_user('Grace')
        print ''
        self.new_game(7)

    # ********************************************************
    # COMMAND: exit
    # ********************************************************
    def do_exit(self, line):
    	return True

    # ********************************************************
    # COMMAND: exit
    # ********************************************************
    def postcmd(self, stop, line):
    	print('')
    	print('USERS:')
    	for id in self.users:
            self.users[id].print_user()
        print('')
        return stop


# ********************************************************
# ROUTINE: main
# ********************************************************
def main():   
    global gSevenUp
    gSevenUp = SevenUp()
    gSevenUp.initialize()
    gSevenUp.cmdloop()
    gSevenUp.shutdown()

# ********************************************************
# ROUTINE: main
# ********************************************************
if __name__ == '__main__':
    main()
