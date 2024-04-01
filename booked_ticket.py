class Star_cinema:
    hall_list=[]
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats={}
        self.show_lists=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        super().__init__()

    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.show_lists.append(show)

        self.seats[id] = []
        
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                col.append(0)
            self.seats[id].append(col)

    def view_show(self):
        print('TODAY SHOW IS HERE')
        for show_list in self.show_lists:
            print(f'MOVIE NAME: {show_list[1]}({show_list[0]})   MOVIE ID: {show_list[0]}  TIME: {show_list[2]}')

    def view_available_seat(self,id):
        if id not in self.seats:
            print('Plaese enter a valid ID')
        else:
             for seat in self.seats[id]:
                 print(seat)

    def book_ticket(self,id,row,col):
          if id not in self.seats:
            print('Please enter a valid show id.')
            return

          if not(1 <= row <= self.rows and 1 <= col <= self.cols):
            print('Please select a valid seat.')
            return
            
          if self.seats[id][row-1][col-1] == 0:
            self.seats[id][row - 1][col - 1] = 1
            print(f'Seat {row,col} booked successfully for the show {id}.')
          else:
            print('Sorry, this seat already booked.')

obisari=Star_cinema()
hall1=Hall(5,5,1)
obisari.entry_hall(hall1)

hall1.entry_show(101,'Blue battle','10:00 AM')
hall1.entry_show(202,'Openheimer','3:00 PM')
hall1.entry_show(303,'Aquaman','8:00 PM')


while True:
     print("1. VIEW ALL SHOW TODAY")
     print("2. VIEW AVAILABLE SEATS")
     print("3. BOOK TICKET")
     print("4. EXIT")

     op=int(input('ENTER YOUR OPTION:'))
     if op==1:
        hall1.view_show()
     elif op==2:
        id=int(input('ENTER ID:'))
        hall1.view_available_seat(id)

     elif op==3:
          id=int(input('ENTER ID:'))
          row = int(input("Pleaase Enter seat row :"))
          col = int(input("Pleaase Enter seat col :"))
          hall1.book_ticket(id,row,col)
     elif op==4:
         break