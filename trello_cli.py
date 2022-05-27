from Trello import Trello
import sqlite3
def greet():
    print('------------------------------')
    print('Trello Command Line Interface: ')
    print('------------------------------')
    print('You are working on '+ board['name'])
    print('Tip: select a List to operate on Trello board.')

#this is an auxiliar function to generate the sql insert command for sqlite.
#it receives the name of the table, and the list of values to insert.
def sqlite_insert(table,values):
    text='INSERT INTO '+table+' VALUES ('
    size = len(values)
    count=0
    for value in values:
        text = text +'"'+ value +'"'
        if (size-1!=count):
            text+=','
        else:
            text+=')'
        count+=1
    return text
def sqlite_delete(table,id):
    text='DELETE FROM '+table+' WHERE id= "'+id+'"'
    return text
    #sqlite syntax
    #DELETE FROM stocks WHERE stockid=1

def new_card_cli(idList):
    name = None
    while (not name):
        name = str(input('Type the name of the card: '))
        if (name): 
            break
        print('The name of the card cannot be empty!')
    desc = str(input('Type the description of the card (optional): '))
    try:
        card=trello.new_card(idList,name,desc)
        values=(card['id'],card['name'],card['desc'],card['idBoard'],card['idList'])
        #print(sqlite_insert('cards',values))
        cur.execute(sqlite_insert('cards',values))
        con.commit()
    except:
        raise

def display_cards(idList,option):
    cards=trello.get_cards(idList)
    print('------------------------------')
    print('List: ' + lists[option-1]['name'])
    for card in cards:
        print('---title: '+ card['name'])
        print('---description: '+card['desc'])
    print('------------------------------')

def delete_card(idList):
    cards=trello.get_cards(idList)
    for card in cards:
        try:
            trello.delete_card(card['id'])
            cur.execute(sqlite_delete('cards',str(card['id'])))
            con.commit()
            #print(sqlite_delete('cards',card['id']))
        except:
            raise

main_menu = {
    1: 'Problems',
    2: 'Working',
    3: 'Ready',
    4: 'Exit Trello CLI'
}
act_menu = {
    1: 'Display cards',
    2: 'Add new card',
    3: 'Delete cards',
    4: 'Go back'
}

def actions_menu(idList,option1):
    while(True):
        for key in act_menu.keys():
            print ('  ',str(key), '--', act_menu[key])
        option2 = int(input('Enter your choice: '))
        if option2==1:
            display_cards(idList,option1)
        elif option2==2:
            new_card_cli(idList)
        elif option2==3:
             inp = str(input('this will delete all cards in the current list. confirm? (y/n)'))
             if (inp=='y'):
                 delete_card(idList)
             else: 
                 break
        elif option2==4:
            break
        else:
             print('Invalid option. Please enter a number between 1 and 4.')

trello=Trello('6136c9e1d3934b88f006963d3ab2aa2d','6ee8664fa7dd091a9353667eba31d360b22c9c983c6c62a1902334ec553b324e','vzsjBgwW')
board=trello.get_board()
lists=trello.get_lists()

#connect to the database, if the database is not created, or if the name has changed it will be.
con = sqlite3.connect('trello.db')
cur = con.cursor()

sqlcommand='''CREATE TABLE IF NOT EXISTS "cards" (
	"id"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"desc"	TEXT,
	"id_board"	TEXT NOT NULL,
	"id_list"	TEXT NOT NULL,
	PRIMARY KEY("id")
)'''

cur.execute(sqlcommand)
con.commit()


#main while loop, only way out is selecting exit option(4) or CTRL + C
greet()
while (True):
    for key in main_menu.keys():
            print (key, '--', main_menu[key] )

    option1 = int(input('Enter your choice: '))
    #after a few refactors this was the cleaner way to do it.
    if option1==1:
        print('You selected option 1.')
        actions_menu(lists[0]['id'],option1)
    elif option1==2:
        print('You selected option 2.')
        actions_menu(lists[1]['id'],option1)
    elif option1==3:
        print('You selected option 3.')
        actions_menu(lists[2]['id'],option1)
    elif option1==4:
        print('Closing...')
        con.close()
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')

