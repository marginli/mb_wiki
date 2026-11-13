---
title: 價值編碼（valence coding）
created: 2026-11-13
updated: 2026-11-13
tags: [concept, active, mb-learning]
confidence: medium
---

# 價值編碼（valence coding）

**價值（valence）指一個刺激、一顆神經元或一筆記憶代表「好」還是「壞」，以及有多好、多壞；價值編碼是說腦用哪些細胞的活動來表示這個正負。** 本庫最常用的版本是：每型蕈狀體輸出神經元（MBON）被活化時推動果蠅靠近（正價值）或走開（負價值），學習改變某型 MBON 收到的輸入，整個 MBON 群體就偏向一邊（「價值平衡」或「偏斜」模型）。這裡的「價值」不是「重要性」的意思。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **MBON**：蕈狀體輸出神經元，讀出 Kenyon 細胞（KC）的訊號。學習改變的是 KC→MBON 突觸。
- **DAN、PAM、PPL1**：多巴胺神經元；PAM 群多半傳獎賞，PPL1 群多半傳懲罰。
- **先天價值／習得價值**：天生就喜歡或討厭（例如蘋果醋天生被喜歡）／學來的好壞。
- **PI**：偏好指數，正值表示偏向某側（見 [[c-performance-index]]）。
- **側角（lateral horn）**：處理先天氣味反應的腦區。

## 怎麼判定

庫內有三種操作型定義，量的東西不同：

1. **MBON 的行為價值**：在未受訓的動物上以光人工活化某型 MBON，看靠近或走開（成蟲用 PI，Aso 2014b；幼蟲用轉彎與爬行速度，Eschbach 2021）。
2. **DAN 的價值**：DAN 對懲罰、獎賞與氣味的放電升降，並與該氣味的行為價值（另一批果蠅在小球上的轉向）作相關（Huang 2024）。
3. **模型中的價值**：Minnick 2026 定義為（推動趨近的 MBON 每步脈衝總數 − 推動躲避的 MBON 每步脈衝總數）÷ 正規化常數。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mbon-valence]] | 逐型以光活化 MBON 量 PI，再做雙型組合 | 讓果蠅走開的全是麩胺酸 MBON，靠近的全是 GABA 或乙醯膽鹼 MBON；MBON 的方向「一般而言」與同格 DAN 寫入的記憶相反；相反方向的組合大致相加 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 拿 Aso 2014b 的分類對照自己量到的突觸減弱 | MBON-γ1pedc 推動靠近，懲罰配對後它對 CS+ 的反應下降，與躲避一致（未自行檢驗行為效果） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 以末梢鈣成像看 γ 葉各格 DAN 對糖、電擊與掙扎的反應 | γ2/γ3 與 γ4/γ5 的 DAN 呈相反樣式；作者主張 DAN 以群體、雙向的樣式代表情境與狀態，而不是各格各代表一種價值 |
| [[s-handler-2019-dopamine-receptor-timing]] | 用「γ4 MBON 推動走開、γ2 推動靠近」解讀迎風行為的方向 | 時序決定 γ4 突觸變強或變弱，行為的正負跟著翻轉 |
| [[s-aso-2016-dan-cell-type-rules]] | 改變同一型 DAN 與氣味的先後 | PPL1-γ1pedc 在氣味後放電造成躲避，在氣味前 20–60 秒放電反而造成喜好：DAN 寫下的價值不固定 |
| [[s-felsenberg-2017-re-evaluation]] | 以「價值偏斜」模型解釋糖記憶的消退 | 消退寫下一筆帶嫌惡價值的新記憶，抵銷原本的偏好 |
| [[s-felsenberg-2018-memory-extinction]] | 量 MBON 對 CS+ 的反應，追蹤兩筆相反價值的記憶 | 舊的嫌惡記憶與新的消退記憶並存，在 M6 這顆 MBON 上相加 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 在無多巴胺的 TH 突變果蠅活化 DAN | PPL1-γ1pedc 改寫出正價值記憶、PAM-γ5 反之（價性反轉），歸因於共同傳遞物一氧化氮 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | 幼蟲逐型光活化 MBON 分正負，再用電顯找同時收 MBON 與側角輸入的匯聚神經元 | 正價值 8 顆、負價值 6 顆（論文以型計為 6 與 5）；約 10 型匯聚神經元收正價值 MBON 興奮、負價值 MBON 抑制與側角興奮 |
| [[s-huang-2024-dopamine-memory-dynamics]] | 電壓成像量 5 型 PPL1 對電擊、糖與五種氣味的放電 | 電擊升、糖降，越討厭的氣味 DAN 放越多；MBON 的氣味反應與價值無關。作者主張 DAN 把先天與習得價值相加 |
| [[s-aso-2023-upwind-neurons]] | 記錄 UpWiN 對兩型 MBON 的反應 | 單一神經元把獎賞區 MBON-α1 的抑制與嫌惡區 MBON-α3 的興奮加減起來 |
| [[s-yamada-2023-second-order-conditioning]] | 由二階記憶跨多個區室反推 | 作者主張二階制約學到的是「廣義的正價值」，不是特定獎賞（迴路推論） |
| [[s-minnick-2026-untrained-connectome]] | 在連結體模型中以上式算價值 | 只給增強、不給氣味，價值也掉到 −0.29：原樣版的學習不是聯結式的 |

> 參數見 [[numbers]]。

## 引用時的陷阱

1. **MBON 的價值是人工活化的行為效果，不是它對好氣味、壞氣味的自然反應。** Aso 2014b 與 Eschbach 2021 都這樣定義。Huang 2024 甚至量到 MBON 對五種氣味的反應幅度與價值無關。
2. **「MBON 方向與同格 DAN 相反」的證據比它的名氣弱。** 能直接比對單型的格只有 γ1pedc、γ2α′1、γ4。只標 MBON-α1 的品系單獨活化時果蠅沒有偏好，卻是 2 小時糖記憶所需（見 [[s-ichinose-2015-reward-recurrent-circuit]] 的整理）。
3. **「相加」不是全部成立。** Aso 2014b 同方向的 5 組組合中有 2 組不符合正文「更強」的判準（見該頁 3.3）。
4. **DAN 的價值不是固定標籤。** 時序（Aso 2016、Handler 2019）與有沒有多巴胺（Aso 2019）都能讓同一型 DAN 寫下相反的記憶；Cohn 2015 認為 DAN 是群體樣式，不是各格一種價值。
5. **鈣成像看不到 DAN 放電的下降。** Huang 2024 延伸圖 13 顯示同一型 DAN 對喜歡的氣味放電明顯下降，鈣訊號幾乎不變。以鈣成像判定「DAN 不編碼負價值」要附條件。
6. **整合發生在哪裡，各篇答案不同：** DAN 上（Huang 2024）、蕈狀體下游的匯聚神經元（Eschbach 2021，幼蟲）、UpWiN（Aso 2023）。發育階段與細胞層級不同，Eschbach 2021 來源頁判定不構成矛盾，但「唯一的整合點」這種說法沒有來源支持（見 [[t-innate-learned-integration]]）。
7. **幼蟲的區室不是成蟲的區室。** Eschbach 2021 的正負價值 MBON 不能直接套到成蟲的 α/β、γ 葉。
8. **Aso 2014a 的「匯聚區是先天與習得價值相遇處」只有影像重疊**，沒有找出任何同時收兩邊輸入的細胞（見 [[s-aso-2014-mb-architecture]] 主張四）。

## 相關

- 主題：[[t-innate-learned-integration]]、[[t-mbon-to-action]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]、[[t-timing-rules]]
- 概念：[[c-appetitive-memory]]、[[c-prediction-error]]、[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-feedforward-inhibition]]、[[c-cs-us-timing]]
- 實體：[[e-mbon]]、[[e-dopaminergic-neuron]]、[[e-mbon-gamma1pedc]]、[[e-mbon-gamma4]]、[[e-mbon-alpha1]]、[[e-mbon-alpha3]]、`e-vt1211`
- 綜述：[[syn-contradictions]]
