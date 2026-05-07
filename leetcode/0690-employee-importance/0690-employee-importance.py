class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {e.id: e for e in employees}
        def dfs(eid):
            e = d[eid]
            ans = e.importance
            for sub_id in e.subordinates:
                ans += dfs(sub_id)
            return ans
        return dfs(id)