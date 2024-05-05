

class Pegs:

    def __init__(self, pegs, plates):
        self.pegs=pegs
        self.plates=plates
        self.moves=[(0,0)] # include a 'neutral move' at beginning
        self.peg1=list(range(self.plates))
        self.peg1.reverse()
        self.Pegs=[self.peg1]+ [[] for _  in range(self.pegs-1)]
        self.maxheight=self.plates+1
        
    def draw(self):
        vrows=[]
        width = self.plates
        for i_inv in range(self.maxheight):
            rowstring=""
            peglength=self.maxheight-i_inv #runs from maxheigh to 1
            for peg in self.Pegs:
                if(len(peg)< peglength):
                    rowstring+=(width*" " + "|" +  width*" ")
                else:
                    pl=peg[peglength-1]
                    rowstring+=(width-pl)*" " + (2*pl+1)*"#"+(width-pl)*" "
            vrows.append(rowstring)

        for row in vrows:
            print(row)

#how many times do bottom tile move (once)
#how many times do second to bottom til move (twice)
#how many times do third to bottom tile move (four times wiht three pegs, seems to be four times with four pegs )
#how ... fourth form bottom (appears to be 8 times with four pegs)
# how .... fifth (moves twice?)
# how... sixth (moves four times ? )

#So you have a top block being treated as once version of four-pegs solution, and a bottom part being treated as a three peg version.
#the optimal cut between topblock and bottom block can presumably be found by lookin at the difference equations. 

#Otherwise maybe prove that interlacing will always cost you more moves. 

#can this be proven by induction (fastest way to clear two with n tiles is fastest way to clear two with n-1 + 1 + fastest one to move two 
#with n-1 tiles. )

    def is_finished(self):
        return len(self.Pegs[0])==1 and len(self.Pegs[-1])==0         #print()
        #return len(self.Pegs[0])==1 and (min([len(p) for p in self.Pegs[1:]])==0)  
        #by symmetry it is enough to find sequence where only largest plates
        #is left on initial peg, and at least one other peg is clear

    def get_moves(self):
        cmoves=[]
        for i,a in enumerate(self.Pegs):
            for j,b in enumerate(self.Pegs):
                if(len(a)>0):
                    if(len(b)==0 or b[-1]>a[-1]):
                        cmoves.append((i,j))
        return cmoves
    
    def make_move(self,move):
        elt=self.Pegs[move[0]].pop()
        self.Pegs[move[1]].append(elt)
        self.moves.append(move)

    def undo_move(self,move):
        elt=self.Pegs[move[1]].pop()
        self.Pegs[move[0]].append(elt)
        self.moves.pop()

    def key(self):
        return str(self.Pegs)
    
    def update(self, newPegs):
        self.moves=newPegs.moves.copy()
        self.Pegs = [peg.copy() for peg in newPegs.Pegs]  

def find_moves(pegs=4, plates=8):
    visited_configurations=set()
    p=Pegs(pegs,plates)
    next_configuration_queue =[p]
    while(len(next_configuration_queue)>0):
        pt=next_configuration_queue.pop()
        moves=pt.get_moves()
        for move in moves:
            q=Pegs(pegs,plates)
            q.update(pt)
            q.make_move(move)
            if(q.is_finished()):
                print(len(q.moves)-1)
                return {"pegs":pegs,"plates":plates,"moves":q.moves}
            if(q.key() in visited_configurations):
                continue
            next_configuration_queue = [q] + next_configuration_queue
        visited_configurations.add(pt.key())

#Maybe start at either end and check when they meet. But either end will be either all on first pegs, or largest plate on initial, some shuffle of plates on remainng, and one peg free. 
#Maybe try Djikstra or a* to speed it up. 
#Would be nice if we had some sort of metric giving us a form of triangle inequality. 
import os
def run_moves(result):
    pp=Pegs(result["pegs"],result["plates"])
    for move in result["moves"]:
        os.system("clear")#possible cls on some operating systems
        pp.make_move(move)
        pp.draw()
        input("press key to see next move")


