---
title: 突觸前末梢的鈣（presynaptic calcium）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, cross-domain]
confidence: medium
---

# 突觸前末梢的鈣（presynaptic calcium）

**神經元要從軸突末梢（突觸前，送出訊號的一側）放出傳遞物質之前，末梢裡的鈣會先升高；所以在軸突或末梢上量鈣，常被當成「這裡送出了多少訊號」的間接讀數。** 本庫用它來看兩件事：多巴胺有沒有改變 KC 末梢的反應（也就是改變是否發生在突觸前），以及 MBON 輸出端的反應在學習與消退後怎麼變。它是間接指標：鈣升高不等於一定放出更多傳遞物質。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體、KC、葉、區室**：蘑菇體（mushroom body）是果蠅腦中把氣味和好壞經驗連起來的構造；代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」，每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ4、α1），細胞以所在區室命名（見 [[e-mushroom-body]]、[[c-mb-compartment]]）。
- **常見詞**：PAM／PPL1＝兩群多巴胺神經元（DAN），分別多傳遞獎賞／懲罰；光遺傳＝讓神經元帶上照光就放電的蛋白（[[e-cschrimson]]）；離體＝把腦取出泡在養液裡，活體＝活果蠅固定後看腦；順向配對＝氣味先、多巴胺後，逆向＝多巴胺先；「未配對」＝兩種刺激錯開、不同時出現；cAMP＝多巴胺受體被活化後在細胞內產生的訊號小分子；※ 推論＝本庫推得、原文沒明說，？待查＝要靠其他資料確認。
- **KC、MBON、DAN**：Kenyon 細胞、蘑菇體輸出神經元、多巴胺神經元（見 [[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]）。
- **GCaMP**：遇鈣變亮的螢光蛋白（見 [[e-gcamp]]）；**sytGCaMP** 是 Cohn 2015 把它接在只待在突觸小泡上的蛋白 synaptotagmin 上，只在末梢發光。
- **forskolin**：直接活化製造 cAMP 的酵素的藥。
- **區室**：葉沿長度切成的一格，例如 γ2–γ5（見 [[c-mb-compartment]]）。
- **CS+／CS−**：訓練時配了電擊的氣味／對照氣味。

## 怎麼算 / 怎麼判定

在軸突所在的葉或區室（不是細胞體）劃範圍，量刺激（乙醯膽鹼或氣味）引起的螢光變化 ΔF/F0；比較多巴胺（或 cAMP 藥物、訓練）前後，或比較同一條軸突在不同區室的反應。sytGCaMP 把讀數限在末梢；一般 GCaMP 量的是整段軸突的胞質鈣。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 離體腦；G-CaMP 1.6 表現於 KC（238Y），乙醯膽鹼噴萼部，在 α、α′ 葉與萼部量鈣；比較 forskolin 或多巴胺前後 | forskolin 使 α 葉反應約 3.2 倍、多巴胺約 2 倍（從圖判讀）；作者稱「突觸前可塑性」，但 forskolin 下萼部（樹突）也增強 |
| [[s-cohn-2015-coordinated-neuromodulation]] | sytGCaMP 表現於 γ KC，雙光子體積成像逐區室量末梢；活體給氣味、離體給乙醯膽鹼；吃糖、活化 58E02 DAN、DopR2 突變 | 活體中同一條軸突 γ2/γ3 末梢反應強、γ4/γ5 弱，界線對齊 γ3/γ4；離體時大致均勻；吃糖或活化 γ4/γ5 DAN 使分布偏向 γ4/γ5；DopR2 突變使樣式倒轉 |
| [[s-felsenberg-2018-memory-extinction]] | 活體 GCaMP 量 M4β′、M6 等 MBON 的**軸突**（輸出端），與樹突比較 | 只訓練時 M6 軸突對 CS+ 的反應較大、樹突沒有差別；消退後 M6 軸突的差別不顯著、M4β′ 軸突仍在；作者的解釋：另一顆會抑制 M6 的 MBON（MVP2）把突觸接在 M6 樹突根部附近，學習讓 MVP2 變安靜，M6 的「煞車」在這個關口鬆開，所以變化只在關口下游的軸突看得到（電顯解剖支持接點位置，見 [[e-mbon-gamma5beta2a]]） |

> 對照：[[s-hige-2015-heterosynaptic-plasticity]] 量的是 KC **細胞體**的鈣（離突觸遠，配對後沒有配對專屬的改變）；[[s-handler-2019-dopamine-receptor-timing]] 在 KC 軸突量的是**內質網內**的鈣（ER-GCaMP，變暗＝放鈣），不是胞質鈣。兩者都不是本頁意義的突觸前讀數，故不列入表。數值見 [[numbers]]。

## 引用時的陷阱

1. **Tomchik 2009 的增強不是突觸增強。** 它沒有量 KC→MBON 傳遞，而且萼部也一起變強，「只在突觸前」的說法比資料強（見 [[c-kc-mbon-plasticity]] 陷阱 1）。
2. **Cohn 2015 的末梢樣式是正規化後的相對值。** 四區室的變化加總約為零，所以「γ2 下降」不是獨立證據；而且配對（氣味＋DAN）之後的末梢鈣該篇沒有量。因此它推進了「多巴胺會改變末梢鈣」，沒有回答「配對造成的減弱在突觸哪一側」（見 [[t-dopamine-to-plasticity]]）。
3. **Felsenberg 2018 的「抵銷」是不顯著，不是相等**；混合標記（VT1211）的軸突也不顯著，但 M4β′ 單獨仍顯著。
4. **鈣感測器版本與讀法不同，數值不能跨篇比**：G-CaMP 1.6、sytGCaMP（GCaMP6s）、GCaMP6f／6m（見 [[e-gcamp]]）。
5. **「末梢鈣升高」與「放出更多傳遞物質」之間還隔一步**，三篇都沒有直接量釋放量。

## 相關

- 概念：[[c-kc-mbon-plasticity]]、[[c-camp-signaling]]、[[c-mb-compartment]]、[[c-ex-vivo-explant]]、[[c-whole-cell-patch-clamp]]
- 實體：[[e-gcamp]]、[[e-kenyon-cell]]、[[e-dopamine-receptor]]、[[e-r58e02]]、[[e-mbon-gamma5beta2a]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-memory-updating]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]
