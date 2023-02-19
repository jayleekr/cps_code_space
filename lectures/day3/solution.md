# HW-#3 Solutions

## Soltuion 1

```python
cpc= {
    "1-team": ["수림", "카이", "진배", "라라진", "박작가", "주혜"],
    "2-team": ["승철", "선현", "봉호", "경진", "만두", "진용", "쩡아", "민경"],
    "3-team": ["선현", "의현", "밀라", "의선", "의영", "성희", "태진"]
}

print("Solution 1")
print(f"1-team's leader : {cpc['1-team'][0]}")
print(f"1-team's all members : {cpc['1-team']}")
print(f"2-team's leader : {cpc['2-team'][0]}")
print(f"2-team's all members : {cpc['2-team']}")
print(f"3-team's leader : {cpc['3-team'][0]}")
print(f"3-team's all members : {cpc['3-team']}")

# Output
1-team's leader : 수림
1-team's all members : ['수림', '카이', '진배', '라라진', '박작가', '주혜']
2-team's leader : 승철
2-team's all members : ['승철', '선현', '봉호', '경진', '만두', '진용', '쩡아', '민경']
3-team's leader : 선현
3-team's all members : ['선현', '의현', '밀라', '의선', '의영', '성희', '태진']

```

## Solution 2

```python
def solution2(allmembers : list, leaders: list) -> int:
    '''Solution 2
    # leaders = "수림", "승철", "선현"
    # all members : 카이, 진배, 라라진, 박작가, 주혜, 선현, 봉호, 경진, 
    # 만두, 진용, 쩡아, 민경, 승철, 의현, 밀라, 의선, 의영, 성희, 태진, 수림
    cpc = {
    "1-team": {
        "leader": "SomeLeader1"
        "members": ["SomeLeader1", "SomeMember1", "SomeMember2", "SomeMember3", "SomeMember4", "SomeMember5", "SomeMember6"]
    },
    "2-team": {
        "leader": "SomeLeader2"
        "members": ["SomeLeader2", "SomeMember7", "SomeMember8", "SomeMember9", "SomeMember10", "SomeMember11", "SomeMember12"]
    },
    "3-team": {
        ...
    }
    Input : all members, leaders 
    '''
    cpc={}
    index=1
    for leader in leaders:
        cpc[f"{index}-team"] = {"leader": leader, "members": [leader]}
        index+=1
        while True:
            if len(allmembers) == 0:
                break
            member = allmembers.pop()
            if member == leader:
                continue
            if len(cpc[f"{index-1}-team"]["members"]) > 7:
                break
            cpc[f"{index-1}-team"]["members"].append(member)
    
    print("Solution 2")
    print(f"1-team's leader : {cpc['1-team']['leader']}")
    print(f"1-team's all members : {cpc['1-team']['members']}")
    print(f"2-team's leader : {cpc['2-team']['leader']}")
    print(f"2-team's all members : {cpc['2-team']['members']}")
    print(f"3-team's leader : {cpc['3-team']['leader']}")
    print(f"3-team's all members : {cpc['3-team']['members']}")
    return 0


mem_str="카이, 진배, 라라진, 박작가, 주혜, 선현, 봉호, 경진, 만두, 진용, 쩡아, 민경, 승철, 의현, 밀라, 의선, 의영, 성희, 태진, 수림"
mem_list = mem_str.split(",")
leader_list = ["수림", "승철", "선현"]
solution2(mem_list, leader_list)


# Output
1-team's leader : 수림
1-team's all members : ['수림', ' 수림', ' 태진', ' 성희', ' 의영', ' 의선', ' 밀라', ' 의현']
2-team's leader : 승철
2-team's all members : ['승철', ' 민경', ' 쩡아', ' 진용', ' 만두', ' 경진', ' 봉호', ' 선현']
3-team's leader : 선현
3-team's all members : ['선현', ' 박작가', ' 라라진', ' 진배', '카이']

```