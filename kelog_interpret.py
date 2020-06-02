file = 'Log_results.txt'
buffer = []

def main():
    try:
        with open(file, 'r') as log:
            for each_line in log:
                with open("./log_interpreted.txt", 'w') as interpret:
                    output = each_line.strip()
                    if output == 'Key.space':
                        output = ' '
                    elif output == 'Key.shift':
                        output = '\n*Shift*\n'
                    elif output == 'Key.esc':
                        output = '\n*Esc*\n'
                    elif output == 'Key.ctrl_l':
                        output = '\n*Ctrl*\n'
                    elif output == 'Key.caps_lock':
                        output = '\n*Caps Lock*\n'
                    elif output == 'Key.tab':
                        output = '\n*Tab*\n'
                    elif output == 'Key.backspace':
                        output = '\n*Backspace*\n'
                    elif output == 'Key.enter':
                        output = '\n'
                    elif output == 'Key.f1':
                        output = ' *\nF1\n* '
                    elif output == 'Key.f2':
                        output = '\n*F2*\n'
                    elif output == 'Key.f3':
                        output = '\n*F3*\n'
                    elif output == 'Key.f4':
                        output = '\n*F4*\n'
                    elif output == 'Key.f5':
                        output = '\n*F5*\n'
                    elif output == 'Key.f6':
                        output = '\n*F6*\n'
                    elif output == 'Key.f7':
                        output = '\n*F7*\n'
                    elif output == 'Key.f8':
                        output = '\n*F8*\n'
                    elif output == 'Key.f9':
                        output = '\n*F9*\n'
                    elif output == 'Key.f10':
                        output = '\n*F10*\n'
                    elif output == 'Key.f11':
                        output = '\n*F11*\n'
                    elif output == 'Key.f12':
                        output = '\n*F12*\n'
                    elif output == 'Key.home':
                        output = '\n*Home*\n'
                    elif output == 'Key.end':
                        output = '\n*End*\n'
                    elif output == 'Key.down':
                        output = '\n*Down Arrow*\n'
                    elif output == 'Key.up':
                        output = '\n*Up Arrow*\n'
                    elif output == 'Key.right':
                        output = '\n*Right Arrow*\n'
                    elif output == 'Key.left':
                        output = '\n*Left Arrow*\n'
                    else:
                        output = each_line[1:2]
                    buffer.append(output)
                    interpret.writelines(buffer)
        print('log_interpreted.txt file created\n')
        with open('log_interpreted.txt') as finalfile:
            for each_line in finalfile:
                print(each_line)

    except FileNotFoundError as err:
        print('Error: File Not Found. Please Enter a Valid Filename.')
        main()


if __name__ == '__main__':
    main()
