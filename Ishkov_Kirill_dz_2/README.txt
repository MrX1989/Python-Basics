������������.
� 3-�� ������� �� ������� ����� ����������� ���������� " ����� list.insert(pos - 1, '"')
���� ��������� �������� ��������� ������� ��������� �� �����������. ������ ���������� ��� ���� �� ��������� �������� "�������" ����� ��������� ������.

my_text = ['�', '5', '�����', '17', '�����', '�����������', '�������', '����', '+5', '��������']
pos = 0
while pos < len(my_text):
    if my_text[pos].isdigit():
        my_text.insert(pos - 1, '"')
	my_text[pos] = my_text[pos].zfill(2)
        my_text.insert(pos + 1, '"')
    elif my_text[pos][1:].isdigit():
        my_text.insert(pos - 1, '"')
	my_text[pos] = my_text[pos].zfill(3)
        my_text.insert(pos + 1, '"')
    pos += 1

print(*my_text)