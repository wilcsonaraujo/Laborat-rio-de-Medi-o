query_repositorios = """
query {
    search(query:"stars:>100", type:REPOSITORY, first:100){
        nodes{
          ... on Repository
            {
                name
                nameWithOwner
                primaryLanguage {
                    name
                }
            }
        }
    }
}
"""