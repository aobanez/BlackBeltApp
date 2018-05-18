    

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

Values = Sessions_Attended ['sessions']

sessions = Values.split(',')

Session_Count = len(sessions)

string = "I have attended " + str(Session_Count) + " Sessions."

print(string)
