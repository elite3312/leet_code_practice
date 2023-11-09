
class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        bit_strings=["{0:b}".format(elem) for elem in data]
        
        for i in range(len(bit_strings)):
            if len(bit_strings[i])!=8:
                bit_strings[i]='0'*(8-len(bit_strings[i]))+bit_strings[i]
        
        print(bit_strings)

        #bit_string_count=0
        sniff_state='init'#"saw_n"
        byte_checks=0
        
        n=0
        for i,elem in enumerate(bit_strings):
            if sniff_state=='init':
                if elem.startswith('0'):
                    #bit_string_count+=1
                    
                    continue
                elif elem.startswith('1'):
                    first_ones=elem.split('0')[0]
                    n=len(first_ones)
                    if n >4:return False
                    sniff_state="saw_n"
                    if i==len(bit_strings)-1:return False
                if elem.startswith('10'):
                    return False
            elif sniff_state=='saw_n':
                if elem.startswith('10'):
                    byte_checks+=1
                    if (i==len(bit_strings)-1) and (byte_checks!=n-1):return False
                    if byte_checks==n-1:
                        
                        byte_checks=0
                        #bit_string_count+=1
                        sniff_state='init'
                else: return False
            
                              
        return True
if __name__ == "__main__":
    
    s = Solution()
    #data=[250,145,145,145,145]
    data=[240,162,138,147,17]
    #data = [197,130,1]
    #data=[240,162,138,147,145]
    ans=s.validUtf8(data)
    print(ans)
    