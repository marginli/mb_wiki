---
title: 獎賞記憶（appetitive memory）
created: 2026-11-13
updated: 2026-11-13
tags: [concept, active, mb-learning]
confidence: medium
---

# 獎賞記憶（appetitive memory）

**果蠅把一個氣味（或顏色）和好事連起來之後，再遇到它就偏向它走，這筆記憶叫獎賞記憶，也譯作欲求記憶。** 本庫的「好事」主要是糖；也有以光活化獎賞型多巴胺神經元（PAM 群）或糖味覺神經元代替糖的人工版本。它和電擊造成的嫌惡記憶共用蕈狀體，但所需的細胞、時間進程與實驗條件都不同，不能直接互換。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **CS+／CS−**：訓練時配糖的氣味／同樣聞但不配糖的對照氣味。
- **PAM、PPL1**：兩群多巴胺神經元（DAN）。PAM 群多半傳獎賞，PPL1 群多半傳懲罰（只是整群的傾向）。
- **MBON**：蕈狀體輸出神經元，推動果蠅靠近或走開。
- **飢餓處理**：訓練前讓果蠅禁食。果蠅要餓才學得會、也才表現得出糖記憶，所以每篇都先餓果蠅。
- **人工獎賞**：不給糖，改用光或熱活化某群神經元當獎賞（見 [[c-us-substitution]]）。
- **PI**：偏好指數，正值表示偏向 CS+（見 [[c-performance-index]]）。

## 怎麼判定

庫內最常見的作法（糖版 T 迷宮，見 [[e-t-maze]]；Ichinose 2015、Felsenberg 2017、Pribbenow 2022、Kaldun 2025）：果蠅先禁食，在管中依序聞 CS− 與 CS+，聞 CS+ 時管內有吸過蔗糖再晾乾的濾紙；之後在兩氣味間選邊，算 PI。四象限競技場（[[e-olfactory-arena]]）與迎風移動是另外兩種讀法。**各篇的禁食時數、糖的形式與測驗時間點都不同**，見陷阱 1。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mbon-valence]] | 逐型阻斷 MBON，測 2 小時氣味—糖、顏色—糖與氣味—酒精三種獎賞記憶 | 需要很多型（氣味配糖 8 條品系、顏色配糖 5 條、酒精 8 條）；三種都需要 M4/M6 麩胺酸 MBON。作者稱「嫌惡集中、獎賞分散」，但篩檢流程不對稱，證據中等 |
| [[s-burke-2012-octopamine-dopamine-reward]] | 以 [[e-shibire-ts]] 阻斷、`e-dtrpa1` 活化章魚胺神經元，對照蔗糖與「甜而無熱量」的阿拉伯糖 | 章魚胺只負責糖的甜味那一份，且在 PAM 多巴胺神經元的上游；活化章魚胺造的記憶撐不過 3 小時，活化 PAM 則在無章魚胺的突變株照樣成形 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 一次糖訓練後，分階段阻斷 α/β KC、[[e-mbon-alpha1]]、[[e-pam-alpha1]] | 三者在訓練時與訓練後 1 小時內都必要，只影響 24 小時記憶、不影響 5 分鐘記憶；作者提出 PAM-α1→KC→MBON-α1→PAM-α1 迴圈 |
| [[s-aso-2016-dan-cell-type-rules]] | 以光活化單型 PAM（α1、β1/β2、γ5/β′2a）代替糖，比較六項學習性質 | PAM-α1 學得慢、記得穩，連學兩組氣味都記得；α1、β1/β2 的記憶一天後仍留一部分 |
| [[s-handler-2019-dopamine-receptor-timing]] | 以光活化 PAM 配蘋果醋氣味，量迎風距離 | 一次配對即可改變追氣味的程度，方向與懲罰 DAN 相反；順序對調（DAN 在前）時方向也翻過來 |
| [[s-felsenberg-2017-re-evaluation]] | 糖訓練後 3 小時再聞 CS+ 或 CS−、不給糖 | 再聞 CS+ 造成消退；再聞 CS− 使記憶進入可被冷休克破壞的再鞏固期 |
| [[s-felsenberg-2018-memory-extinction]] | 電擊記憶消退時阻斷 PAM 群（[[e-r58e02]]） | 消退需要 PAM，作者把消退記憶視為一筆**獎賞記憶**（「該來的懲罰沒來」被記成好事）；這是依 PAM 需求與 M6 變化方向所作的解讀 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 在無多巴胺的 TH 突變果蠅活化懲罰型 PPL1-γ1pedc | 果蠅反而學會喜歡該氣味（價性反轉）；據此找到共同傳遞物一氧化氮 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | 在 M4/6 降低乙醯膽鹼受體次單元，對照糖與電擊記憶 | 降 α5 時立即記憶就學不起來，降 α2、α1 或 Dlg 時 3 小時記憶消失；同樣處理對電擊記憶幾乎無影響 |
| [[s-yamada-2023-second-order-conditioning]] | 以糖或光活化 PAM-α1 寫一階記憶，再做二階制約 | α1 的一階記憶經 SMP353/354、SMP108 活化別格的獎賞 DAN，教出二階記憶（見 [[c-second-order-conditioning]]） |
| [[s-aso-2023-upwind-neurons]] | 在四個區室分別以光寫入獎賞記憶，並以糖訓練、`e-tnt` 阻斷 UpWiN | 四組 PI 都顯著，只有 α1 與 β1β2 兩組會迎風走向氣味 |
| [[s-kaldun-2025-dop1r2-memory-phases]] | 在各葉條件式剔除 Dop1R2，測糖記憶 0、2、24 小時 | 立即記憶不受影響；2 小時起 α/β、α′/β′ 剔除組下降，γ 不受影響。2 小時獎賞記憶剩 53–59%，嫌惡剩 15–21%（本庫由圖判讀計算，論文未檢定兩者差異） |
| [[s-tumkaya-2025-synthetic-memory-inception]] | 紅光活化嗅覺受體神經元當氣味，藍光活化 PAM（R58E02-LexA）當獎賞 | 全人工獎賞記憶在兩台裝置都成立：ΔPI +0.50（MOT）、+0.38（WALISAR） |

未列入：[[s-cohn-2015-coordinated-neuromodulation]] 與 [[s-huang-2024-dopamine-memory-dynamics]] 只拿糖當刺激，量 DAN 的反應，沒有做獎賞記憶；[[s-gervasi-2010-pka-dynamics]] 與 [[s-tomchik-2009-camp-dynamics]] 只把章魚胺當獎賞的代用品加在 KC 上（見 [[c-octopamine-reward-signal]]）。

> 參數見 [[numbers]]。

## 引用時的陷阱

1. **飢餓處理各篇不同，分數不宜並排。** 禁食時數：Burke 2012 為 18–20 小時；Felsenberg 2017 為 18–24 小時；Kaldun 2025 為 19–21 小時；Pribbenow 2022 為 20–24 小時；Aso 2016 方法寫 24–48 小時、圖 4 圖說寫 48 小時；Yamada 2023 為 40–48 小時。Ichinose 2015 與 Aso 2014b 改以死亡率為準：前者餓到測試時死亡 5–15%，後者約 10%（圖 7 圖說寫 28–40 小時）。Aso 2016 光活化 PAM 的實驗是否先餓過，PDF 沒有明說。
2. **24 小時記憶的「中間餵食」也不同。** Burke 2012 訓練後先餵 3 小時、再禁食 21 小時；Kaldun 2025 也是先餵 3 小時再餓。不同的餵食安排會改變測驗時的動機，跨篇比較 24 小時分數前要先對齊。
3. **「糖」不是單一訊號。** Burke 2012 把甜味與熱量拆開：阻斷章魚胺只在阿拉伯糖訓練時有影響。Ichinose 2015 引言也說，有營養的糖一次就能形成長期記憶，沒營養的只形成短期記憶。引用「糖獎賞需要 X」時要寫明用的是哪一種糖。
4. **人工獎賞不等於糖。** 光活化單型 PAM 留下的記憶性質，不代表真糖訓練時的分工（Aso 2016 自承）；Aso 2023 量 UpWiN 可塑性用的 R58E02-LexA 會叫醒多格 PAM，不只 α1。Tumkaya 2025 的全人工記憶比自然學習弱。
5. **PI 顯著不代表果蠅會主動靠近。** Aso 2023 四組 PI 都顯著，卻只有兩組迎風。只用二選一分數，看不到記憶叫出的是哪種動作（見 [[t-mbon-to-action]]）。
6. **「獎賞記憶靠突觸後」只是推測。** Pribbenow 2022 據受體降低與 KC 阻斷的差別推測獎賞記憶靠突觸後、電擊記憶可能靠突觸前；最直接的突觸後證據只有約 6% 的增強，方向還與活體學習相反（見該頁第五節）。
7. **「消退記憶是獎賞記憶」是解讀。** Felsenberg 2018 的證據是「需要 PAM」與「M6 的變化方向和糖學習相同」；活體內 γ5 DAN 的教學訊號沒量到。

## 相關

- 主題：[[t-dopamine-to-plasticity]]、[[t-memory-updating]]、[[t-mbon-dan-feedback]]、[[t-mbon-to-action]]、[[t-timing-rules]]
- 概念：[[c-valence-coding]]、[[c-prediction-error]]、[[c-second-order-conditioning]]、[[c-us-substitution]]、[[c-octopamine-reward-signal]]、[[c-memory-extinction]]、[[c-memory-consolidation]]、[[c-performance-index]]、[[c-mb-compartment]]
- 實體：[[e-pam-alpha1]]、[[e-mbon-alpha1]]、[[e-r58e02]]、`e-dtrpa1`、`e-tnt`、[[e-t-maze]]、[[e-olfactory-arena]]、[[e-dopamine-receptor]]
- 綜述：[[syn-contradictions]]
- 待開頁面：`e-pam-cluster`、`c-sweet-vs-nutrient`
