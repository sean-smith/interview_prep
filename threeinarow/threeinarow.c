#include <stdio.h>
#include <stdlib.h>
// Tic-Tac-Tree
// You score 1 point if there are three consecutive same color squares
// Squares can be consecutive vertical, horizontal or diagonal
// Squares are either red or black as defined below:

// I'm assuming that N >= 3 since anything less has no score
// I'm assuming that the board is arranged as follows:
// 0 = red
// 1 = black

// Example:
// 101
// 111 => Black score 5, red scores 0
// 101

int check_diagonal(int color, int x, int y, int N, int board[][N]);
int check_horizontal(int color, int x, int y, int N, int board[][N]);
int check_vertical(int color, int x, int y, int N, int board[][N]);



int red_wins(int N, int board[][N]) {
	// score of {red, black}
	int score[2] = {0,0};
	
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			score[board[y][x]] += check_diagonal(board[y][x], x, y, N, board);
			score[board[y][x]] += check_horizontal(board[y][x], x, y, N, board);
			score[board[y][x]] += check_vertical(board[y][x], x, y, N, board);
		}
	}
	printf("Red scored: %d\nBlack scored: %d\n", score[0], score[1]);
	
	return score[0] > score[1];
}

int check_diagonal(int color, int x, int y, int N, int board[][N]) {
	int score = 0;
	if ((N - y >= 3) && (N - x >= 3)) {
		if (color == board[y + 1][x + 1] && color == board[y + 2][x + 2]) {
			score++;
		}
	}
	if ((N - y >= 3) && (x + 1 >= 3)) {
		if (color == board[y + 1][x - 1] && color == board[y + 2][x - 2]) {
			score++;
		}
	}
	return score;
}

int check_horizontal(int color, int x, int y,  int N, int board[][N]) {
	int score = 0;
	if ((N - x >= 3)) {
		if (color == board[y][x + 1] && color == board[y][x + 2]) {
			score++;
		}
	}
	return score;
}

int check_vertical(int color, int x, int y,  int N, int board[][N]) {
	int score = 0;
	if ((N - y >= 3)) {
		if (color == board[y + 1][x] && color == board[y + 2][x]) {
			score++;
		}
	}
	return score;
}

int main()
{
	int N = 3;
	int board[3][3] = {
		{1, 0, 1},
		{1, 1, 1},
		{1, 0, 1}
	};

	 if(red_wins(N, board)) {
	 	printf("Red wins\n");
	 }
	 else {
	 	printf("Black wins\n");
	 }

	return 0;
}