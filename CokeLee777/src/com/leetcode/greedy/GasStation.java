package com.leetcode.greedy;

/**
 * https://leetcode.com/problems/gas-station/
 */
public class GasStation {

    public static class MySourceCode{

        public int canCompleteCircuit(int[] gas, int[] cost) {
            int stationLen = gas.length;

            for(int startIdx = 0; startIdx < stationLen; startIdx++){
                //시작위치에서 기름이 존재하지 않는다면 무시
                if(gas[startIdx] == 0) continue;
                //현재 남아있는 기름
                int restGas = gas[startIdx];
                //방문한 정거장의 수
                int visited = 0;
                //현재 정거장 인덱스
                int nowIdx = startIdx;

                //한바퀴를 여행할때까지 반복
                //다음 정거장으로 이동하는데, 다음 정거장으로 이동할 수 없다면 시작위치 변경
                while(visited++ < stationLen && (restGas -= cost[nowIdx++]) >= 0){
                    //현재 인덱스가 범위를 벗어난다면
                    nowIdx = (nowIdx == stationLen ? 0 : nowIdx);
                    //아니라면 다음 정거장으로 이동
                    restGas += gas[nowIdx];
                }
                //한바퀴를 다 돌았다면 시작위치 반환후 종료
                if(visited > stationLen) return startIdx;
            }
            //시작할 수 있는 정거장이 없다면 -1반환
            return -1;
        }
    }

    public static class Solution{

        public int canCompleteCircuit(int[] gas, int[] cost) {
            int n = gas.length;
            int total_surplus = 0;
            int surplus = 0;
            int start = 0;

            for(int i = 0; i < n; i++){
                //total_surplus: 전체 정거장을 다 돌수 있는지 판단
                total_surplus += gas[i] - cost[i];
                //현재 정거장까지 여행할 수 있는 기름이 모자라는지 판단
                surplus += gas[i] - cost[i];
                //기름이 모자르면 초기화 후 출발 정거장 변경
                if(surplus < 0){
                    surplus = 0;
                    start = i + 1;
                }
            }
            //정거장을 다 여행할 수 없다면 -1반환 아니면 출발 정거장 반환
            return (total_surplus < 0) ? -1 : start;
        }
    }
}
