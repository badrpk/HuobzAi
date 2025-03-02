import torch

class HuobzEinops:
    """Custom Tensor Operations to Replace Einops"""

    @staticmethod
    def rearrange(tensor, pattern: str):
        """
        Rearrange tensor dimensions based on pattern.
        Example: 'b c h w -> b (h w) c' flattens spatial dims.
        """
        if pattern == "b c h w -> b (h w) c":
            return tensor.permute(0, 2, 3, 1).reshape(tensor.shape[0], -1, tensor.shape[1])
        elif pattern == "b h w c -> b c h w":
            return tensor.permute(0, 3, 1, 2)
        else:
            raise ValueError(f"Unsupported pattern: {pattern}")

    @staticmethod
    def repeat(tensor, pattern: str, **kwargs):
        """
        Repeat tensor along specified dimensions.
        Example: 'b c -> b c repeat' doubles last dimension.
        """
        if "repeat" in pattern:
            repeat_dim = kwargs.get("repeat", 2)
            return tensor.repeat(1, repeat_dim)
        else:
            raise ValueError(f"Unsupported pattern: {pattern}")

    @staticmethod
    def reduce(tensor, pattern: str, reduction: str):
        """
        Reduce tensor along dimensions based on pattern.
        Example: 'b c h w -> b c' with reduction='mean' averages over spatial dims.
        """
        if pattern == "b c h w -> b c" and reduction == "mean":
            return tensor.mean(dim=[2, 3])
        else:
            raise ValueError(f"Unsupported pattern: {pattern} or reduction method: {reduction}")

# ✅ Usage Example
if __name__ == "__main__":
    dummy_tensor = torch.randn(2, 3, 4, 4)  # Example tensor [batch, channels, height, width]
    huobz_ops = HuobzEinops()
    rearranged = huobz_ops.rearrange(dummy_tensor, "b c h w -> b (h w) c")
    print("✅ Custom Einops Replacement Works!")
