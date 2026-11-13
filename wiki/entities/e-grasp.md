---
title: 跨突觸夥伴 GFP 重組（GFP Reconstitution Across Synaptic Partners, GRASP）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# 跨突觸夥伴 GFP 重組（GRASP）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **GFP**：綠色螢光蛋白。GRASP 把它拆成兩段，各段單獨不發光。
- **GAL4、LexA**：兩套互不干擾的基因開關，可以在兩群不同的細胞各自表現不同的東西。「LexAop-」「UAS-」分別是受 LexA、GAL4 開啟的基因。
- **突觸前、突觸後**：一個突觸送出訊號的一側與接收的一側。末梢（軸突端）通常是送出，樹突通常是接收。
- **ampr、SIP、SLP**：腦區縮寫。ampr 是前內側原腦（anterior medial protocerebrum；Burke 2012 推測 0104 品系標記的 PAM 多巴胺神經元樹突在此）；SIP、SLP 是上中間與上外側前大腦。
- **PAM、MB-MP1、MBON-α1**：PAM 群多巴胺神經元多傳遞獎賞；MB-MP1 是 PPL1-γ1pedc 的舊名（[[e-ppl1-gamma1pedc]]）；MBON-α1 是 α1 區室的輸出神經元（[[e-mbon-alpha1]]）。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認。

## 是什麼

**GRASP 讓兩群細胞各帶 GFP 的一段，只有兩者的細胞膜貼得夠近時，兩段才拼成會發光的 GFP，用來找可能的接觸點。** Ichinose 2015 的試劑是 UAS-CD4::spGFP1-10 與 LexAop-CD4::spGFP11，分別由 GAL4 與 LexA 品系驅動。兩篇來源頁都強調：**它顯示的是「相鄰」，不等於有突觸**；兩位作者自己的措辭也只是「可能的突觸接觸位置」（Burke 2012：plausible sites of synaptic contact）與「緊密相鄰」（Ichinose 2015：close juxtaposition）。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-burke-2012-octopamine-dopamine-reward]] | Tdc2-LexA（章魚胺神經元）分別配 0104-GAL4（標記一群 PAM 多巴胺神經元的品系）與 c061-GAL4;MBGAL80（MB-MP1）；圖 4i 與補充圖 S10（本庫未取得） | 兩組都在 ampr 出現強訊號；MB-MP1 這組另在蕈狀體腳跟有訊號。用來支持「章魚胺在 ampr 作用於多巴胺神經元」 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | R72D01-LexA（PAM-α1）配 MB310C（MBON-α1），共軛焦影像用 Olympus FV1200 | SIP、SLP 與 α1 區室都有訊號（圖 2F），支持 PAM-α1 與 MBON-α1 有接觸 |

兩篇都只用它做解剖支持，都沒有接著用電顯確認突觸。

## 已知的問題

- **分不出方向。** GRASP 只說兩片膜貼近，不說誰送誰收。Ichinose 2015 的 α1 區室內那團訊號，依兩型細胞在該處的極性推，若是突觸方向會是 PAM-α1 → MBON-α1，與作者要證明的「MBON-α1 回饋到 PAM-α1」相反（※ 推論，見該來源頁）；SIP／SLP 那條訊號才是回饋的候選位置。
- **陽性不等於功能性突觸。** Burke 2012 圖 4i 的訊號集中在 ampr 兩側，但圖上沒有突觸層級的證據。Ichinose 2015 正文先寫「緊密相鄰」，同一節後面卻寫成確定的「單突觸回饋」（⚠️ 該篇自身不一致，見 [[s-ichinose-2015-reward-recurrent-circuit]]）。
- **訊號歸屬取決於品系涵蓋範圍。** 若 R72D01-LexA 另標其他 PAM 型，SIP／SLP 的訊號可能部分來自非 α1 的 PAM（※ 推論，見 Ichinose 2015 來源頁）；Burke 2012 的排除推論同樣建立在品系涵蓋範圍上（見 [[syn-contradictions]] 1.4、1.5）。
- **補充圖未取得。** Burke 2012 的 GRASP 有一部分在補充圖 S10，本庫未取得，只能轉述正文。

## 相關

- 比較：[[e-mcfo]]（看形態與重疊）、[[e-hemibrain]]、[[e-catmaid]]（電顯，可數突觸）
- 品系：[[e-split-gal4]]
- 細胞：[[e-mbon-alpha1]]、[[e-pam-alpha1]]、[[e-ppl1-gamma1pedc]]
- 主題：[[t-mbon-dan-feedback]]
- 來源：[[s-burke-2012-octopamine-dopamine-reward]]、[[s-ichinose-2015-reward-recurrent-circuit]]
- 概念：[[c-octopamine-reward-signal]]
- 待開頁面：`e-tdc2-gal4`、`e-mb310c`
