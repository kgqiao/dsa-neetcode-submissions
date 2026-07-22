class Solution:
    def encode(self, strs: List[str]) -> str:
        # Handle the empty list edge case
        if not strs:
            return "EMPTY_LIST"
            
        encoded = []
        for s in strs:
            # Pair each string with its length to protect against delimiter collision
            encoded.append(f"{len(s)}:{s}")
            
        # Join with a standard delimiter safely
        return "+".join(encoded)

    def decode(self, s: str) -> List[str]:
        # Handle the empty list edge case
        if s == "EMPTY_LIST":
            return []
            
        result = []
        # Split by the primary delimiter
        parts = s.split("+")
        
        i = 0
        while i < len(parts):
            # Find the length prefix before the colon
            length_str, text = parts[i].split(":", 1)
            length = int(length_str)
            
            # Reconstruction logic handles cases where a '+' was inside the original string
            while len(text) < length:
                i += 1
                text += "+" + parts[i]
                
            result.append(text)
            i += 1
            
        return result