def stableInternships(interns, teams):
    # Write your code here.
    n = len(interns)

    intern_to_team = [-1 for _ in range(n)]
    team_to_intern = [-1 for _ in range(n)]

    assigned_count = 0

    while assigned_count < n:

        i = 0
        while intern_to_team[i] != -1:
            i += 1

        f_free_intern = i

        j = 0
        while j < n and intern_to_team[f_free_intern] == -1:
            team = interns[f_free_intern][j]

            if team_to_intern[team] == -1:
                team_to_intern[team] = f_free_intern
                intern_to_team[f_free_intern] = team
                assigned_count += 1
            else:
                current_intern = team_to_intern[team]
                if teams[team].index(f_free_intern) < teams[team].index(current_intern):
                    team_to_intern[team] = f_free_intern
                    intern_to_team[f_free_intern] = team
                    intern_to_team[current_intern] = -1

            j += 1

    return_list = []
    for i in range(n):
        return_list.append([i, intern_to_team[i]])

    return return_list