st = {1, 2, 3, 4, 5}
st2 = {2, 3, 10}


print(st2.issubset(st))
print(st.issuperset(st2))

print(st.symmetric_difference(st2))


st3 = {i for i in range(1, 11) if i % 2 == 0}
print(st3)
