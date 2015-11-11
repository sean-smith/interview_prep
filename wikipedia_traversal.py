# Given that Wikipedia Pages are defined as:
class WikipediaPage(object):
    def __init__(self, other_pages=[]):
        self.other_pages = other_pages
        self.visited = False
    
# and a start WikipediaPage (start) and a destination WikipediaPage
# (destination), find the fewest number of links that needed to be
# clicked to get from the start to destination.

def find_fewest_clicks(start_page, destination_page):
    if (start_page == destination_page):
        return  0
    l = []
    for page in start_page.other_pages:
        if not page.visited:
            page.visited = True
            l.append(1 + find_fewest_clicks(page, destination_page))
    print l 
    return min(l)


golden_gate = WikipediaPage([])
mission = WikipediaPage([golden_gate])
sf = WikipediaPage([mission, golden_gate])
california = WikipediaPage([sf])
usa = WikipediaPage([california])

print "California -> Golden Gate =", find_fewest_clicks(california, golden_gate)

# golden_gate = []
# sf = [golden_gate]
# california = [sf]
# oregon = [usa]
# usa = [oregon, california, golden_gate]

# Test Cases:
# find_fewest_clicks([],SF)
# find_fewest_clicks(usa, golden_gate)
# find_fewest_clicks(usa, usa) => 0
# find_fewest_clicks(usa, golden_gate) => 1