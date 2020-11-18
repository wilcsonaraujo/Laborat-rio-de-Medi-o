query_issues = """
{
    repository(name: "{placeholder_nome_repo}", owner: "{placeholder_owner_repo}") {
        issues(orderBy: {field: COMMENTS, direction: {placeholder_orientacao_issue}}, first: 50) {
            nodes {
                number
                id
                comments {
                    totalCount
                }
                title
            }
        }
    }
}
"""


