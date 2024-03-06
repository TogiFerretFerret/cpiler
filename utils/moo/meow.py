from colorama import Fore, Style, Back
def imacow():
    """
    Prints a cow ASCII art and a message.

    This function prints a cow ASCII art along with the message "Meow Meow I'm a cow" and a warning message "CHEATING IS BAD. STOP HACKING".

    Example usage:
    >>> imacow()
    Meow Meow I'm a cow
      _________
    | Meow Meow |                
      =========                  
             \\
              \\
                ^__^             
                (oo)\_______     
                (__)\       )\/\\
                    ||----w |    
                    ||     ||    
    CHEATING IS BAD. STOP HACKING
    """
    print(Back.GREEN + Fore.CYAN + Style.BRIGHT + "Meow Meow I'm a cow" + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + Style.NORMAL + """
  _________
| Meow Meow |                
  =========                  
         \\
          \\
            ^__^             
            (oo)\_______     
            (__)\       )\/\\
                ||----w |    
                ||     ||    """ + Style.RESET_ALL)
    print(Back.GREEN + Fore.CYAN + Style.BRIGHT + "CHEATING IS BAD. STOP HACKING" + Style.RESET_ALL)
    