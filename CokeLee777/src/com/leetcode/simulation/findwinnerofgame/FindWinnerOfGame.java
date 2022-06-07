package com.leetcode.simulation.findwinnerofgame;

public class FindWinnerOfGame {

    static class MySourceCode{

        public int getWinner(int[] arr, int k) {

            int winCount = 0;
            int currentWinner = arr[0];
            for(int i = 1; i < arr.length; i++){
                // TODO : 연승할 경우 카운트 1증가
                if(currentWinner > arr[i]) winCount++;
                else {
                    winCount = 1;
                    currentWinner = arr[i];
                }

                // TODO : k연승 한 경우 리턴
                if(winCount == k) return currentWinner;
            }
            return currentWinner;
        }
    }
}
