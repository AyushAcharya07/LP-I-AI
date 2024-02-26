import java.util.Scanner;
 
class Board {
 
    int chessBoard[][];
    int queens;
 
    public Board(int queens) {
        chessBoard = new int[20][20];
        this.queens = queens;
    }
 
    void displayBoard(){
        int i, j;
        for(i=0; i<queens; i++){
            for(j=0; j<queens; j++){
                if(chessBoard[i][j] == 1)
                    System.out.print(" Q ");
                else
                    System.out.print(" - ");
            }
            System.out.print("\n");
        }
        System.out.print("\n");
        System.out.print("\n");
    }
 
    void reset(){
        for(int i=0; i<queens; i++){
            for(int j=0; j<queens; j++){
                chessBoard[i][j] = 0;
            }
        }
    }
 
    boolean isValidPlace(int row, int col){
        int i,j;

        for(i=col; i>=0; i--){
            if(chessBoard[row][i] == 1)
                return false;
        }
 
        for(i=row, j=col; i>=0 && j>=0; i--,j--){
            if(chessBoard[i][j] == 1)
                return false;
        }
 
        for(i=row, j=col; i<queens && j>=0; i++,j--){
            if(chessBoard[i][j] == 1)
                return false;
        }
 
        return true;
    }
}
 
class NQueen {
 
    int queens;
    boolean flag;
    Board board;
 
    public NQueen(int queens) {
        this.flag = false;
        this.board = new Board(queens);;
        this.queens = queens;
    }
 
    void solveNqueen(){
 
        int i;
        hasSolution(0,0);
        if(!flag)
            System.out.println("No Solution");
 
    }
 
    boolean hasSolution(int ctr, int colQueen){ 
        if(colQueen == queens){
            flag = true;
            board.displayBoard();
            return false;
        }
 
        int i,j;
        for(i=ctr; i<queens; i++){
            if(board.isValidPlace(i,colQueen)){
                board.chessBoard[i][colQueen] = 1;
                if(hasSolution(0,colQueen+1))
                    return true;
 
                //backtrack
                board.chessBoard[i][colQueen] = 0;
            }
 
        }
        return false;
    }
}
 
public class Puzzle {
 
    static Scanner in = new Scanner(System.in);
 
    public static void main(String args[]){
        System.out.println("Enter number of Queens");
        int queens = in.nextInt();
 
        NQueen nQueen = new NQueen(queens);
        nQueen.solveNqueen();
 
    }
}
