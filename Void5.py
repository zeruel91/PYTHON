import numpy as np
class integer:
    def question(self):
        self.constant = np.random.randint(-10,10,2)
        self.pm = np.random.randint(5)
        self.exponent = np.random.randint(2,5)
        if self.pm == 0:
            print('{} + {} ?'.format(self.constant[0],self.constant[1]))
            
        elif self.pm == 1:
            print('{} - {} ?'.format(self.constant[0],self.constant[1]))
            
        elif self.pm ==2:
            print('{}*{} ?'.format(self.constant[0],self.constant[1]))
            
        elif self.pm == 3:
            print('{}/{} ?'.format(self.constant[0],self.constant[1]))
            
        else:
            print('{}^{} = ?'.format(self.constant[0],self.exponent))
        

    def answer(self):
        if self.pm == 0:
            result = self.constant[0] + self.constant[1]
            return str(result)
        elif self.pm == 1:
            result = self.constant[0] - self.constant[1]
            return str(result)
            
        elif self.pm == 2:
            result = self.constant[0] * self.constant[1]
            return str(result)
          
        elif self.pm == 3:
            result = self.constant[0] / self.constant[1]
            return str(result)
        else:
            result = self.constant[0] ** self.exponent
            return str(result)
        
a = integer()
a.question()

while True:
    x = input('your answer :')
    b = a.answer()
    
    if x == b:
        print('its correct')
        break
    else:
        print('incorrect. the correct answer is {}'.format(b))

