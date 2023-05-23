A diferença dos resultados entre as multiplicações tex1 * tex2 e mul(tex1, tex2) está relacionada à forma como as operações são interpretadas em HLSL. A primeira operação (tex1 * tex2) multiplica as texturas elemento por elemento, enquanto a segunda (mul(tex1, tex2)) opera na multiplicação dos valores resultantes da amostragem das texturas.

Referencias:

https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-operators#multiplication-operator-

https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-intrinsic-functions#mul
