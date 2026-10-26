---
title: split-GAL4 驅動品系（split-GAL4 driver lines）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# split-GAL4 驅動品系（split-GAL4 driver lines）

## 是什麼

**驅動品系**是決定「某個外加基因只在哪些神經元表現」的果蠅品系。GAL4 是一種能開啟目標基因的蛋白；在哪些細胞裡製造它，取決於接在前面的調控序列。一般的 GAL4 品系常同時標到很多種細胞。

**split-GAL4** 把 GAL4 拆成兩半：一半負責「抓住 DNA」（DBD），一半負責「啟動表現」（AD），各由一段不同的調控序列控制。只有兩段序列都開啟的細胞，兩半才湊得成完整的 GAL4（Hige 2015 的說明）。這樣能把表現範圍縮到少數幾型、甚至一顆神經元。在本庫，它主要用來只讓特定的 [[e-dopaminergic-neuron]]（DAN）帶上光敏感通道 [[e-cschrimson]]。

另一套互不干擾的系統 LexA 常與它並用：GAL4 標 DAN，LexA 標要記錄的 MBON 或 KC。

## 版本與規模（本庫用到的品系）

| 品系 | 來源 | 兩半各由什麼控制（AD／DBD） | 標記什麼 |
|---|---|---|---|
| **MB320C** | Hige 2015 寫「we created」；Aso 2016 把它的影像指向 Aso et al. 2014a | TH／22B12 | **只標一顆 PPL1-γ1pedc**（[[e-ppl1-gamma1pedc]]） |
| **MB099C** | Hige 2015 新做 | TH／73F07 | ⚠️ 兩篇說法不同：Hige 2015 說**四型 PPL1**（γ2α′1、α′2α2、α′3、α3），Aso 2016 說 PPL1-γ2α′1 ＋ PPL1-α′2α2 **兩型**；兩篇都說它不標 PPL1-γ1pedc。見 [[e-mb099c]]、[[syn-contradictions]] 1.4 |
| MB438B | 先前文獻（Aso et al. 2014a）中 PPL1-γ1pedc 的專一品系 | AD 插在 attP40（基因組上預先設好、供外加基因插入的固定位置） | Hige 2015 **刻意不用**，理由見下 |
| **MB042B** | Handler 2019 | R58E02／R22E04 | PAM 群（涵蓋哪些區室，論文沒列：？待查）；AD 半與 [[e-r58e02]] 同一段序列 |
| **MB504B** | Handler 2019；Felsenberg 2017、2018 也用 | 52H03／TH | Handler：PPL 群中**支配六個區室**的一部分（沒列哪六個）；Felsenberg 2017 延伸圖 6c：四型 PPL1（γ1pedc、γ2α′1、α′2α2、α3）。兩者如何對應見 [[e-mb504b]] |
| MB630B | Aso 2016 新做 | VT026773／R72B05 | PPL1-α3（一型） |
| MB043C、MB213B、MB315C＋MB109B | Aso 2016 | 未列 | PAM-α1；支配 β1、β2 的 PAM；支配 γ5、β′2a 的 PAM（後兩組各兩型） |
| MB299B；MB310C、MB323B；MB008B | Ichinose 2015（引 Aso et al. 2014a） | 未列 | PAM-α1（[[e-pam-alpha1]]）；MBON-α1；α/β KC |
| MB296B；MB052B；MB077C；MB112C（延伸圖 6i 寫 MB122C）；MB058B；MB308B | Felsenberg 2017 | 未列 | PPL1-γ2α′1（[[e-ppl1-gamma2alpha1]]）；五型 V2 群 MBON；MBON-γ2α′1（[[e-mbon-gamma2alpha1]]）；MVP2（[[e-mbon-gamma1pedc]]）；PPL1-α′2α2；PPL1-α′3（α3 弱） |

AD／DBD 欄取自兩篇原文的方法與基因型清單（Hige 2015 方法；Handler 2019 STAR Methods 基因型表）。TH 指合成多巴胺的酵素酪胺酸羥化酶的調控序列；22B12、73F07、R58E02、R22E04、52H03 等是調控序列片段的編號（基因型寫成「片段名-AD」「片段名-DBD」）。表中的「一顆」照 Hige 原文 a single neuron；左右腦是否各一顆，原文沒說：？待查。

**常與它並列、但不是 split-GAL4 的品系**：TH-GAL4（[[e-th-gal4]]；Hige 用作正對照，即已知應該有效、用來確認方法可行的組；Handler 與 DDC-Gal4 一起用來在 DAN 表現 VMAT-pHluorin；Felsenberg 2017 用來阻斷 PPL1）；R58E02-GAL4／-LexA（[[e-r58e02]]；標記範圍各篇寫法不同：Handler 2019 基因型表標「γ4–5 DANs」，Cohn 2015 說「包含」支配 γ4、γ5 的一部分 DAN，Felsenberg 2017 延伸圖 6a、6o 說兩個版本都標 13 型 PAM，見 [[syn-contradictions]] 1.5）；73F07-LexA（Handler，γ2 DAN）；VT045661-LexA（Aso 2016，PPL1-γ1pedc）；VT1211-GAL4／-LexA（Felsenberg 2018，M4β′ 與 M6）；Tomchik 2009 的 238Y、c739（[[e-c739-gal4]]）、c305a、1471、c316、GH146 都是一般 GAL4。

## 庫內誰用了它

| 來源 | 用了哪些 | 用來做什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **未使用**（只用一般 GAL4，且沒有操弄 DAN） | — |
| [[s-hige-2015-heterosynaptic-plasticity]] | MB320C、MB099C | MB320C 只活化 γ1pedc 的 DAN，誘發該區 MBON 的突觸變弱；MB099C 活化鄰區 DAN，檢查多巴胺會不會越界，並用來活化 α2 區 |
| [[s-handler-2019-dopamine-receptor-timing]] | MB042B、MB504B | 行為實驗中以光活化 PAM 或 PPL；閉迴路用 MB042B 驅動 ChrimsonR |
| [[s-aso-2016-dan-cell-type-rules]] | MB320C、MB099C、MB630B、MB043C、MB213B、MB315C＋MB109B | 每組品系驅動 CsChrimson，比較各型 DAN 寫入與更新記憶的規則；三組一次活化兩型，因為只活化一型時記憶太弱 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | MB299B、MB310C、MB323B、MB008B | 以 shibire^ts 阻斷（[[e-shibire-ts]]）、RNAi 或 dTrpA1 活化 PAM-α1、MBON-α1、α/β KC |
| [[s-felsenberg-2017-re-evaluation]] | MB504B、MB296B、MB052B、MB077C、MB112C、MB058B、MB308B 等 | 在記憶再活化期間阻斷特定 DAN 或 MBON |
| [[s-felsenberg-2018-memory-extinction]] | MB504B、MB112C | 阻斷 PPL1 群（消退照常）；MVP2 的成像與解剖 |
| [[s-cohn-2015-coordinated-neuromodulation]] | **主文未具名**（稱 sparse driver lines；γ2 DAN、各 γ MBON 的品系名 ？待查） | 讓單一型 MBON 表現 P2X2 或 GCaMP6s |

## 已知的問題（解讀實驗的陷阱）

- **「一個品系」不等於「一型細胞」。** MB099C 同時活化多型 PPL1（幾型，兩篇說法不同，見上表）；Aso 2016 有三組品系各活化兩型；TH-GAL4 標多數 PPL1、少數 PAM 以及蘑菇體以外的許多 DAN。讀到「活化 MB099C」時，要記得是不止一型一起放電。
- **品系不同會混進比較。** Hige 2015 比較 γ1（MB320C，一顆 DAN）與 α2（MB099C，依 Hige 為四型 DAN、依 Aso 2016 為兩型）的誘發門檻（要多少次「氣味＋光」配對才會讓突觸變弱；見 [[e-mushroom-body]]），兩個品系的通道表現量與每次放出的多巴胺量可能不同。行為上，MB099C 代替電擊的效果也遠低於 MB320C（補充圖 S1F：？待查）。Aso 2016 只為 MB320C 與 MB099C 引了放電資料（引 Hige 2015），其餘四組沒有放電或多巴胺釋放的校準，「學得慢」「記得久」的差異可能部分來自活化強度。
- **涵蓋範圍沒有列出。** Handler 2019 的 MB504B（六個區室）與 MB042B 都沒列出支配哪些區室（MB504B 的型別見 Felsenberg 2017 延伸圖 6c，對應方式是 ※ 推論，見 [[e-mb504b]]），而全篇的分子與突觸實驗只在 γ4 做。行為結果可能混有 γ4 以外區室的貢獻，作者也承認行為由多區室合成。
- **插入位點會互相干擾。** Hige 2015 不用 MB438B，因為它的 AD 插在 attP40，與該篇標 MBON 的 LexA 品系同一位點，可能發生 transvection（同源染色體上相同位點的調控元件互相影響），讓 GAL4 與 LexA 在同一批細胞表現；後果是光敏感通道也出現在被記錄的 MBON 上（引 Mellert & Truman 2012）。
- **同一段調控序列可出現在不同品系。** 73F07 是 Hige 的 MB099C 的 DBD，也是 Handler 標 γ2 DAN 的 LexA；25D01 在 Hige 標 MBON-γ2α′1、在 Handler 標「γ2 MBON」。※ 推論：兩篇可能標到相同或重疊的細胞，但 split-GAL4、GAL4 與 LexA 版本的表現範圍不一定相同，兩篇沒有比對：？待查（另見 [[e-mbon]]）。

## 相關

- 工具：[[e-cschrimson]]、[[e-gcamp]]、[[e-shibire-ts]]、[[e-p2x2]]
- 細胞：[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]、[[e-ppl1-gamma1pedc]]、[[e-ppl1-gamma2alpha1]]、[[e-pam-alpha1]]
- 品系：[[e-mb099c]]、[[e-mb504b]]、[[e-r58e02]]、[[e-th-gal4]]、[[e-c739-gal4]]
- 概念：[[c-us-substitution]]、[[c-mb-compartment]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-cohn-2015-coordinated-neuromodulation]]
