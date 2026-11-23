---
title: 局部視覺中間神經元（local visual interneuron, LVIN）
created: 2026-11-24
updated: 2026-11-24
tags: [entity, active, visual-learning]
confidence: medium
---

# 局部視覺中間神經元（local visual interneuron, LVIN）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **LVIN**：自己不伸進視葉、但接收視覺投射神經元（VPN）的輸入再轉交給 Kenyon 細胞（KC）的中央腦中間神經元。
- **VPN**：本體在視葉、軸突伸進中央腦的神經元。見 [[e-visual-projection-neuron]]。
- **直接／間接輸入**：VPN 直接突觸到 KC 為直接；經 LVIN 轉一手為間接。
- **副萼（accessory calyx）**：主萼之外收非嗅覺輸入的小突起；vACA 由 KCγd 的樹突界定，dACA 由 KCα/βp 界定。見 [[e-accessory-calyx]]。
- **APL**：一顆支配整個蕈狀體的 GABA 性大神經元，蕈狀體的增益控制元件。見 [[e-apl-neuron]]。
- **標記**：`※ 推論`＝本庫推得、原文沒明說；`？待查`＝要靠其他資料確認。

## 是什麼

**LVIN 是視覺訊號進蕈狀體的「轉寄」路線。** 名詞首創於 [[s-li-2020-mb-connectome]]（圖 10 圖說與正文），[[s-ganguly-2024-visual-inputs-to-kc]] 的本頁用語明說「定義承自 Li et al. 2020」並沿用計數——**本庫目前這一類的兩篇來源，一篇定義、一篇沿用，沒有第三種用法。**

它存在的理由是兩個視覺副萼走的路完全相反：**vACA 以直接路為主（VPN 46.1% ＞ LVIN 24.6%），dACA 以間接路為主（LVIN 57.8% ≫ VPN 9.8%）。** 換句話說，背側副萼的 KC 幾乎看不到視葉送來的原始訊號，它看到的是被 LVIN 處理過一次的版本。

**兩篇的操作型定義雖然同源，寫法仍不同：**

- [[s-li-2020-mb-connectome]]：「本身接收 VPN 輸入的中介局部視覺中間神經元」——以接線關係定義，沒有寫出排除清單。
- [[s-ganguly-2024-visual-inputs-to-kc]]：篩 FlyWire 超類為 `central`，**明文排除 KC、MBON、DAN、APL、DPM 與嗅覺投射神經元**，且必須有 VPN 輸入。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-li-2020-mb-connectome]] | 在 hemibrain 右半腦把四個萼的輸入拆成扇形，分出「VPN 直接」與「LVIN 間接」兩條路（圖 10、圖 11，不設門檻） | **vACA 的 LVIN 間接佔 24.6%、dACA 佔 57.8%**；圖 10B 顯示 KCγd 樹突上黃點（VPN 直接）與橘紅點（LVIN 間接）在空間上清楚分開，**而圖 11（dACA）的同一格兩色是混在一起的**——這是「兩條路線可以被分別調控」這個推論在 vACA 的唯一解剖依據 |
| [[s-ganguly-2024-visual-inputs-to-kc]] | 在 FlyWire 左半腦逐顆查 KCγ-d 與 KCαβ-p 的上游（門檻 ≥5 突觸），再回查 LVIN 自己的上游 | KCγ-d：**25 個 LVIN（21 個細胞型別）、1,798 個突觸（24.2%）**；最強的 PLP095（FlyWire 名 PLP.78）438 個突觸分布在 24 顆 KCγ-d 上，**而中位數的 LVIN 只有 11 個突觸、分布在 2 顆 KC 上**。KCαβ-p 則是 15 個 LVIN、1,713 個突觸（84%）。LVIN 的上游有 226 個間接 VPN。傳遞物質預測：**19 膽鹼性（76%）、2 GABA（8%）、3 麩胺酸（12%）、1 未知（4%）** |

各篇引用的數字見 [[numbers]]。

## 引用時的陷阱

1. **「有 25 個 LVIN」這句話會嚴重誤導，因為分布極度偏斜。** 最強的一個有 438 個突觸、碰到 24 顆 KC，中位數那一個只有 11 個突觸、碰到 2 顆 KC。**引用個數時要附上「中位數 11 個突觸」這個對照**，否則讀者會以為有 25 條大致等重的轉寄線。
2. **排除清單寫在方法節，而它決定了分母。** [[s-ganguly-2024-visual-inputs-to-kc]] 的 LVIN 定義排除了 APL，所以 APL 的突觸從來沒進過那幾張圓餅；而該篇正文寫 **APL 平均對每顆 KCγ-d 做 16 個（左）、10 個（右）突觸**。`※ 推論`（依據見該頁圖 1 解讀）：若這個平均是對全部 147 顆 KCγ-d 取的，APL 一顆細胞在左半腦就貢獻約 2,352 個突觸，比整個 LVIN 群的 1,798 個還多——**但論文未說明該平均的分母是「全部 KCγ-d」還是「被 APL 接到的 KCγ-d」，若是後者這個乘積會偏高，不確定範圍相當寬。** 引用那幾張圓餅時要說「視覺輸入的組成」，不可說「輸入的組成」。
3. **「有幾個 LVIN 是抑制性的」建立在 25 顆的預測上，每一顆就佔 4%。** 2 個 GABA 與 3 個麩胺酸都是傳遞物質預測的輸出，不是量測（見 [[c-neurotransmitter-prediction]]）。而這個數字有實質後果：**LVIN 是不是抑制性，決定了間接路是加還是減。**
4. **兩篇的 LVIN 不是同一群細胞。** 一篇是 hemibrain 右半腦、一篇是 FlyWire 左半腦，KC 的顆數本身就是未裁決的矛盾 1.14（γd 99 vs 147）。**比例可以對照，名單不能合併。**
5. **間接路不是直接路的備援。** [[s-ganguly-2024-visual-inputs-to-kc]] 圖 3B：49 個直接 VPN 裡有 36 個同時經 LVIN 再送一份——這不是冗餘，因為兩條路的延遲與可能的正負號不同。

## 相關

- 上游：[[e-visual-projection-neuron]]
- 下游與所在構造：[[e-kenyon-cell]]、[[e-accessory-calyx]]、[[e-mushroom-body]]
- 一起競爭分母的細胞：[[e-apl-neuron]]
- 資料集：[[e-hemibrain]]、[[e-fafb]]、[[e-neuprint]]
- 方法：[[c-neurotransmitter-prediction]]、[[e-nblast]]
- 主題：[[t-visual-learning-circuits]]
- 來源：[[s-li-2020-mb-connectome]]（首創此名詞）、[[s-ganguly-2024-visual-inputs-to-kc]]（沿用並計數）
- 待開頁面：`e-flywire`、`e-codex`、`e-lc-neuron`（LC15 只接 1–2 個 LVIN，是「間接路帶特定特徵」的主要例子）
