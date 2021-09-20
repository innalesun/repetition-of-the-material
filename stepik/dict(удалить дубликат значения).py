d = {'id1':
         {'name': ['Sara'],
          'class': ['V'],
          'subject_integration': ['english, math, science']
          },
     'id2':
         {'name': ['David'],
          'class': ['V'],
          'subject_integration': ['english, math, science']
          },
     'id3':
         {'name': ['Sara'],
          'class': ['V'],
          'subject_integration': ['english, math, science']
          },

     'id4':
         {'name': ['Dava'],
          'class': ['V'],
          'subject_integration': ['english, math, science']
          }}

d_new = {}
for x, y in d.items():
    if y not in d_new.values():
        d_new[x] = y

print(d_new)
