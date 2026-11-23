---
title: 副萼（accessory calyx）
created: 2026-11-24
updated: 2026-11-24
tags: [entity, active, visual-learning]
confidence: medium
---

# 副萼（accessory calyx）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **萼（calyx）**：Kenyon 細胞（KC）的樹突區，也就是蕈狀體的收訊端。**主萼（CA）**收嗅覺。
- **副萼（accessory calyx）**：主萼旁邊的小突起，由特定 KC 亞型的樹突界定，收的是非嗅覺輸入。共三個：**vACA**（腹側，視覺）、**dACA**（背側，視覺）、**lACA**（側，溫覺）。
- **uPN／mPN**：投射神經元；uPN 只在單一嗅小球有樹突，mPN 跨多個嗅小球。
- **VPN／LVIN**：視覺投射神經元（直接送）與局部視覺中間神經元（轉一手）。見 [[e-visual-projection-neuron]]、[[e-lvin]]。
- **APL**：支配整個蕈狀體的 GABA 性大神經元，蕈狀體的增益控制元件。見 [[e-apl-neuron]]。
- **標記**：`※ 推論`＝本庫推得、原文沒明說；`？待查`＝要靠其他資料確認。

## 是什麼

**副萼是「蕈狀體不是只管氣味」這件事的解剖位址。** 九成以上的 KC 樹突落在主萼收嗅覺訊號，少數幾群 KC 的樹突另外長在旁邊的小突起上，收視覺或溫覺。副萼因此不是一個獨立器官，而是**由住在裡面的那幾型 KC 定義出來的**：vACA 就是「KCγd 的樹突所在」，換一份連結體、KC 顆數變了，副萼的範圍也跟著變。

**名字有兩套，指的是同一批東西。** [[s-aso-2014-mb-architecture]] 用 **vAC／dAC**，並在圖 7 圖說說明：原本就被叫做「副萼」的那個構造，該篇改名為**背側副萼（dAC）**以與新命名的腹側副萼（vAC）區別。[[s-li-2020-mb-connectome]] 寫成 **vACA／dACA**，並新增第三個 **lACA**（側副萼）。

## 三個副萼（數字取自 [[s-li-2020-mb-connectome]]，hemibrain 右半腦）

| 萼 | 定義它的 KC | 主要感覺輸入 | 總輸入突觸（該頁反推，`※ 推論`） | APL 佔比 |
|---|---|---|---:|---:|
| 主萼 CA（對照） | 1,757 顆 | 嗅覺 uPN 129 條，佔全部輸入 63.6% | ≈267,000 | 9.5% |
| **vACA** | 99 KCγd ＋ 1 KCγs1 | 視覺：VPN 直接 46.1% ＋ LVIN 間接 24.6% | ≈10,850 | 9.1% |
| **dACA** | 60 KCα/βp | 視覺：**LVIN 間接 57.8% ≫ VPN 直接 9.8%** | ≈5,650 | 10.9% |
| **lACA** | 14 KCα′/β′ap1 ＋ 1 KCγs2 | 溫覺：VP3+ vPN 516 ＋ VP2 adPN 412 ＝ **928 個突觸**（超過九成） | ≈1,050 | **0.9%** |

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 以 split-GAL4 與 MCFO 單細胞影像界定七型 KC 的樹突落點，據此命名 vAC 並把舊稱的「副萼」改名為 dAC | γd（約 75 顆）的樹突在主萼腹外側形成 vAC；α/βp（約 90 顆，先驅 KC）的在背外側形成 dAC。**兩個副萼被認為承載非嗅覺訊息，理由是嗅葉主要的嗅覺 PN 不支配它們** |
| [[s-li-2020-mb-connectome]] | 在 hemibrain 右半腦把四個萼的輸入**逐一量化**（圖 9–12，四張圖四段文字，論文從未並列） | 三個副萼的輸入組成如上表；另發現 **lACA 的 APL 佔比只有 0.9%，比其他三個萼低一個數量級**（論文只定性說「比 dACA 與 vACA 少得多」），以及 **lACA 全部 928 個溫覺突觸裡，唯一那顆 KCγs2 一個人收走 268 個（28.9%）**，而它只是 15 顆 KC 中的 1 顆 |
| [[s-ganguly-2024-visual-inputs-to-kc]] | 在 FlyWire 全腦（含視葉）逐顆查兩個視覺副萼的 KC 上游，門檻 ≥5 突觸 | KCγ-d（左 147／右 148 顆）的視覺輸入 **75.8% 走直接路**；KCαβ-p（左 67／右 61 顆）**84% 走間接路**——**「腹側走直接、背側走間接」在第二隻腦上重現**，是兩篇之間最乾淨的交叉驗證 |

各篇引用的數字見 [[numbers]]。

## 引用時的陷阱

1. **拼法有兩套，而 lACA 有年份界線。** vAC/dAC（[[s-aso-2014-mb-architecture]]）與 vACA/dACA（[[s-li-2020-mb-connectome]]）是同一個東西；**側副萼 lACA 在 2014 年那一篇裡不存在**，引用 2014 年前後的「副萼共有幾個」要分開講。
2. **副萼有多大，取決於你用的是哪一份資料。** KCγd 的顆數：約 75（[[s-aso-2014-mb-architecture]]，光學標核計數）／99（hemibrain 右半腦，逐顆計數）／147–148（FlyWire）。⚠️ 矛盾 1.14（未裁決），量法與分型依據都不同，見 [[syn-contradictions]]。
3. **「副萼不收嗅覺輸入」是分類依據，不是零。** [[s-ganguly-2024-visual-inputs-to-kc]] 發現 **147 顆 KCγ-d 中有 5 顆完全沒有視覺輸入，收的是嗅覺投射神經元**（5/147 ＝ 3.4%，該篇沒有檢查這 5 顆的重建品質：`？待查`）；而 [[s-li-2020-mb-connectome]] 圖 2 圖說寫明有 **2 條 PN 支配 lACA**（門檻 25 個突觸）。**「副萼＝非嗅覺」是個好用的第一近似，不是定義上的排除。**
4. **lACA 幾乎不受 APL 控制，而論文沒有展開。** 0.9% 對其他三個萼的 9.1–10.9%。APL 是全蕈狀體的增益控制元件，**溫覺這條通道等於走在一個沒有增益控制的萼裡**——這對「溫覺輸入的增益怎麼調」有直接意義。
5. **兩個視覺副萼的接線邏輯相反，而這個對比要自己算。** 把分母限定在視覺輸入上：vACA 的直接路佔 65.2%、dACA 只佔 14.5%（本庫計算，見 [[s-li-2020-mb-connectome]]）；[[s-ganguly-2024-visual-inputs-to-kc]] 在 FlyWire 對 KCαβ-p 算到 16%。**論文把兩件事分別寫在兩節，從未並列這個比值。**
6. **dACA 收什麼，有一個沒被調和的衝突。** [[s-li-2020-mb-connectome]] 圖 11 圖說自陳「我們無法為『把味覺送進 dACA』找到強候選者」，而該篇引用的 Kirkhart and Scott 2015 報告 KCα/βp 對苦味或甜味有反應。**論文沒有試圖調和這兩件事。**

## 相關

- 住在裡面的細胞：[[e-kenyon-cell]]、[[e-mushroom-body]]
- 輸入：[[e-visual-projection-neuron]]、[[e-lvin]]、[[e-apl-neuron]]
- 資料集：[[e-hemibrain]]、[[e-fafb]]、[[e-neuprint]]
- 概念：[[c-sparse-coding]]、[[c-mb-compartment]]
- 主題：[[t-visual-learning-circuits]]
- 綜述：[[syn-contradictions]]（1.14 視覺 KC 有幾顆、1.15 突觸有沒有爪）
- 來源：[[s-aso-2014-mb-architecture]]、[[s-li-2020-mb-connectome]]、[[s-ganguly-2024-visual-inputs-to-kc]]
- 待開頁面：`e-flywire`、`e-optic-lobe`、`e-accessory-medulla`（副髓質；aMe12 是 KCγ-d 以型別計突觸總數最高的輸入）
