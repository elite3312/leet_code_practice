import base64,pickle


class Solution:
    def encode(self, strs: list[str]) -> str:
        my_layout=strs
        my_layout=pickle.dumps(my_layout)
        my_layout=base64.b64encode(my_layout)
        return my_layout
        #my_layout=str(my_layout,'utf-8')
    def decode(self,layout:str)->list[str]:
        layout = pickle.loads(base64.b64decode(layout))

        return layout

if __name__ == "__main__":
    s = Solution()

    inp = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]
    print(s.encode(inp))
    print(s.decode(s.encode(inp)))

    