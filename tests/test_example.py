from petshop import create_app
from bs4 import BeautifulSoup

expected = dict(id= list(map(int,range(1, 42))),
                name = ['Townsend', 'Bray', 'Garcia', 'Maddox', 'Rodriguez', 'Collins', 'Delgado', 'Harris', 'Hoover', 'Osborn', 'Cole', 'Morgan', 'Beck', 'Martin', 'Davis', 'Snyder', 'Kemp', 'Yates', 'Thomas', 'Bryant', 'Ramos', 'Meadows', 'Scott', 'Fuentes', 'Lopez', 'Johnson', 'Berry', 'Ramsey', 'Brown', 'Russell', 'Leonard', 'Lutz', 'Perry', 'Carpenter', 'Rice', 'Alvarado', 'Rowe', 'Pugh', 'Petersen', 'Perry', 'Perez'],
                bought = ['1980-12-01', '1981-07-30', '1971-06-20', '1982-12-19', '2019-05-24', '1994-10-22', '1976-01-23', '2017-06-21', '1983-07-02', '2002-07-21', '2001-10-23', '2010-09-20', '1997-04-02', '1982-09-14', '1973-01-19', '2003-07-22', '1993-04-30', '1993-11-09', '1983-10-10', '1987-07-17', '1995-09-19', '2014-02-12', '1999-03-06', '1991-08-30', '2017-01-25', '1971-01-03', '1979-12-20', '2019-09-25', '2019-02-18', '1975-09-05','1971-06-10', '2006-06-12', '1986-09-04', '1976-08-19', '2011-05-12', '1986-11-03', '2019-11-20', '1989-09-23', '2014-02-28', '1994-10-02', '2006-02-06'],
                sold = ['1980-12-24', '1981-08-28', '1971-07-01', '', '2019-06-09', '1994-10-28', '', '2017-07-05', '2021-07-10', '', '', '2010-10-09', '', '1982-10-08', '2021-07-03', '', '2021-07-03', '', '2021-07-03', '', '1995-10-04', '2014-02-25', '', '', '2017-02-12', '1971-01-19', '1980-01-08', '2019-10-24', '', '', '', '', '1986-09-14', '', '', '1986-11-25', '2019-12-15', '1989-10-14', '2014-03-21', '', ''],
                species = ['cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'parrot', 'parrot', 'parrot', 'parrot', 'parrot', 'parrot', 'parrot'])


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing



def test_homepage(client):
    resp = client.get("/")
    soup = BeautifulSoup(resp.data, 'html.parser')

    tags = soup.find_all("td", {"class" : "petname"})
    actual = [x.text.strip() for x in tags]
    assert expected['name'] == actual

    tags = soup.find_all("td", {"class" : "petbought"})
    actual = [x.text.strip() for x in tags]
    assert expected['bought'] == actual

    tags = soup.find_all("td", {"class" : "petsold"})
    actual = [x.text.strip() for x in tags]
    assert expected['sold'] == actual

    tags = soup.find_all("td", {"class" : "petspecies"})
    actual = [x.text.strip() for x in tags]
    assert expected['species'] == actual

def test_sorting_name(client):
    ex =expected['name'][:]
    ex.sort()

    resp = client.get("/?order_by=name&order=asc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petname"})
    actual = [x.text.strip() for x in tags]

    assert ex == actual

    resp = client.get("/?order_by=name&order=desc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petname"})
    actual = [x.text.strip() for x in tags]
    ex.sort(reverse=True)
    assert ex == actual

def test_sorting_bought(client):
    ex =expected['bought'][:]
    ex.sort()

    resp = client.get("/?order_by=bought&order=asc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petbought"})
    actual = [x.text.strip() for x in tags]

    assert ex == actual

    resp = client.get("/?order_by=bought&order=desc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petbought"})
    actual = [x.text.strip() for x in tags]
    ex.sort(reverse=True)
    assert ex == actual

def test_sorting_sold(client):
    ex =expected['sold'][:]
    ex.sort()

    resp = client.get("/?order_by=sold&order=asc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petsold"})
    actual = [x.text.strip() for x in tags]

    assert ex == actual

    resp = client.get("/?order_by=sold&order=desc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petsold"})
    actual = [x.text.strip() for x in tags]
    ex.sort(reverse=True)
    assert ex == actual
    
    
def test_sorting_species(client):
    ex =expected['species'][:]
    ex.sort()

    resp = client.get("/?order_by=species&order=asc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petspecies"})
    actual = [x.text.strip() for x in tags]

    assert ex == actual

    resp = client.get("/?order_by=species&order=desc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petspecies"})
    actual = [x.text.strip() for x in tags]
    ex.sort(reverse=True)
    assert ex == actual
    
    
def test_sorting_id(client):
    ex =expected['id'][:]
    ex.sort()

    resp = client.get("/?order_by=id&order=asc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petid"})
    actual = [int(x.text.strip()) for x in tags]

    assert ex == actual

    resp = client.get("/?order_by=id&order=desc")
    soup = BeautifulSoup(resp.data, 'html.parser')
    tags = soup.find_all("td", {"class" : "petid"})
    actual = [int(x.text.strip()) for x in tags]
    ex.sort(reverse=True)
    assert ex == actual
    
    
    
    

def test_details(client):
    resp = client.get("/6")
    soup = BeautifulSoup(resp.data, 'html.parser')
    assert soup.find("u", {"class": "name"}).text == "Collins"
    assert soup.find("span", {"class": "species"}).text.strip() == "cat"
    assert soup.find("h6", {"class": "bought"}).text.strip().replace("\n","") == "Bought on Sat - Oct 22, 1994"
    assert soup.find("span", {"class": "soldstatus"}).text.strip().replace("\n","") == "Sold"
    assert soup.find("span", {"class": "selldate"}).text.strip().replace("\n","") == "Fri - Oct 28, 1994"
    assert soup.find("p", {"class": "description"}).text.strip() == """Peace call property. Authority do environmental generation career. Economy minute possible similar.
Few stay occur quite foot air citizen. Tv network minute lawyer.
Right religious affect American dark baby newspaper. Ability school ever democratic should wish shake. Through charge why law.
Foot edge follow author trip. Chair exist network different matter. Owner appear put him theory him by.
Important pressure cause relationship wait. Oil have miss field drive. Bit practice every beautiful cup between. Level picture reflect carry step.
Effort past sense friend evidence idea trial give. Real future ball contain another. Case bill physical share gas.
Third bar skin. All arm single those southern read more.
Serious travel such. Build individual actually political station interview young power.
Pm also small try but.
Study security safe television money effect concern. Expect work worry leader."""
    assert [a.text.strip() for a in soup.find_all("a", {"class": "tag"})] == ["contest", "adopter", "store pick"]


def test_filter_by_tag(client):
    resp = client.get("/search/tag/contest")
    tags_expected = dict(id= [6,8,10,11,16,18,19,21,28,29,35,36], 
                         name = ["Collins","Harris","Osborn","Cole","Snyder","Yates","Thomas","Ramos","Ramsey","Brown","Rice","Alvarado"],
                         bought = ["1994-10-22","2017-06-21","2002-07-21","2001-10-23","2003-07-22","1993-11-09","1983-10-10","1995-09-19","2019-09-25","2019-02-18","2011-05-12","1986-11-03"],
                         sold = ['1994-10-28', '2017-07-05', '', '', '', '', '2021-07-03', '1995-10-04', '2019-10-24', '', '', '1986-11-25'],
                         species = ["cat","cat","cat","cat","cat","cat","cat","dog","dog","dog","parrot","parrot"])

    soup = BeautifulSoup(resp.data, 'html.parser')

    tags = soup.find_all("td", {"class" : "petname"})
    actual = [x.text.strip() for x in tags]
    assert tags_expected['name'] == actual

    tags = soup.find_all("td", {"class" : "petbought"})
    actual = [x.text.strip() for x in tags]
    assert tags_expected['bought'] == actual

    tags = soup.find_all("td", {"class" : "petsold"})
    actual = [x.text.strip() for x in tags]
    assert tags_expected['sold'] == actual

    tags = soup.find_all("td", {"class" : "petspecies"})
    actual = [x.text.strip() for x in tags]
    assert tags_expected['species'] == actual    

def test_edit_description(client):
    resp = client.get("/11/edit")
    client.post("/11/edit", data ={"description": "dying horde"})
    resp = client.get("/11")
    soup = BeautifulSoup(resp.data, 'html.parser')    
    assert soup.find("p", {"class": "description"}).text.strip() == """dying horde"""

def test_edit_sold(client):
    resp = client.get("/11")
    assert b"Available for sale" in resp.data
    assert b"Sold" not in resp.data

    client.post("/11/edit", data ={"sold": "1"})
    resp = client.get("/11")
    assert b"Sold" in resp.data
    assert b"Available for sale" not in resp.data

