class�Solution:
����def�fib(self,�n:�int)�->�int:
��������a,�b�=�0,�1
��������for�i�in�range(1,�n):
������������a,�b�=�b,�a�+�b
��������return�b
2
