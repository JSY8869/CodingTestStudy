# Greedy - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
## 문제풀이
* 문제풀이 전략
    * 경계로 나뉘는 구간 중 길이가 최대인 구간을 찾음
    * 최대 h와 w를 구한 뒤 곱해줌

* 코드 설명
    1. 경계선을 정렬 후 상하좌우 끝 경계값을 추가해준다.  
    ```
    horizontalCuts.sort()
    verticalCuts.sort()
    
    new_horizontalCuts = [0] + horizontalCuts + [h]
    new_verticalCuts = [0] + verticalCuts + [w]
    ```

    2. 각각의 배열을 순차적으로 탐색하며 h와 w의 최대값을 구해준다.  
    ```
    for i in range(len(new_horizontalCuts) - 1):
        tmp = new_horizontalCuts[i + 1] - new_horizontalCuts[i]
        if tmp > max_h:
            max_h = tmp
            
    for i in range(len(new_verticalCuts) - 1):
        tmp = new_verticalCuts[i + 1] - new_verticalCuts[i]
        if tmp > max_w:
            max_w = tmp
    ```
    
    3. 최대 h와 w를 곱해준 후 조건에 맞게 반환해준다.