def solution(N, stages):
    # 각 스테이지별 실패율을 저장할 리스트 생성
    failure_rate = []
    
    # 스테이지별 실패율 계산
    for stage in range(1, N+1):
        # 도전 중인 플레이어 수
        total_players = len([s for s in stages if s >= stage])
        # 스테이지를 클리어한 플레이어 수
        cleared_players = stages.count(stage)
        
        # 실패율 계산
        if total_players == 0:
            failure_rate.append((stage,0))
        else:
            failure_rate.append((stage, cleared_players / total_players))
    # 실패율을 기준으로 내림차준 정렬, 스테이지 번호를 기준으로 오름차순 정렬
    failure_rate.sort(key=lambda x: (-x[1], x[0]))
    # 정렬된 스테이지 번호 반환
    answer = [stage for stage, _ in failure_rate]
    
    return answer