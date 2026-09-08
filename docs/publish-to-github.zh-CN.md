# 鍙戝竷鍒?GitHub

## 1. 鍙戝竷鍓嶅彧闇€鏇挎崲涓ょ被淇℃伅

鍦ㄤ粨搴撴牴鐩綍鎼滅储 `DaveKingh`锛屾浛鎹㈡垚浣犵殑 GitHub 鐢ㄦ埛鍚嶏紱鍐嶆寜闇€瑕佹妸 `LICENSE` 鍜?`CITATION.cff` 涓殑浣滆€呮敼鎴愪綘鐨勫鍚嶆垨缁勭粐鍚嶃€?

杩愯锛?

```bash
python scripts/validate.py
python scripts/validate.py --response examples/synthetic/expected-output.md
```

涓ゆ潯鍛戒护閮藉簲鏄剧ず `PASS`銆傛浛鎹㈠畬鎴愬悗锛屼笉搴斿啀鍑虹幇 `DaveKingh` 鎻愮ず銆?

## 2. 鐢?GitHub 缃戦〉鍙戝竷锛堟渶閫傚悎绗竴娆★級

1. 鍦?GitHub 鐐瑰嚮 **New repository**銆?
2. Repository name 濉?`paper-evidence-map`銆?
3. Description 浣跨敤 `docs/launch-plan.md` 涓殑鎺ㄨ崘鏂囨銆?
4. 閫夋嫨 **Public**銆?
5. 涓嶈璁?GitHub棰濆鐢熸垚 README銆乣.gitignore` 鎴?License锛屾湰浠撳簱宸茬粡鍖呭惈杩欎簺鏂囦欢銆?
6. 鍒涘缓鍚庢寜 GitHub 椤甸潰鎻愮ず涓婁紶浠撳簱鍏ㄩ儴鍐呭锛屼繚鐣?`.github` 绛変互鐐瑰紑澶寸殑鐩綍銆?
7. 鍦?Settings 鈫?General 鈫?Social preview 涓婁紶鐢?`assets/demo.svg` 瀵煎嚭鐨?1280脳640 PNG銆?
8. 寮€鍚?Issues銆丏iscussions锛屽苟鎸?`docs/publishing-checklist.md` 瀹屾垚鍏朵綑璁剧疆銆?

## 3. 鐢ㄥ懡浠よ鍙戝竷

鍦ㄨВ鍘嬪悗鐨勪粨搴撶洰褰曡繍琛岋細

```bash
git init
git add .
git commit -m "feat: release Paper Evidence Map v0.1.0"
git branch -M main
git remote add origin https://github.com/DaveKingh/paper-evidence-map.git
git push -u origin main
```

鍏朵腑 `DaveKingh` 蹇呴』鏇挎崲涓轰綘鐨勭敤鎴峰悕锛屽苟涓?GitHub 涓婅鍏堝垱寤哄悓鍚嶇┖浠撳簱銆傝嫢浣跨敤 GitHub CLI锛屼篃鍙互鍦ㄦ湰鐩綍杩愯锛?

```bash
gh repo create paper-evidence-map --public --source=. --remote=origin --push
```

## 4. 鍒涘缓棣栦釜 Release

1. 鎵撳紑浠撳簱鐨?Releases 鈫?Draft a new release銆?
2. Tag 濉?`v0.1.0`锛宼arget 閫夋嫨 `main`銆?
3. 鏍囬濉?`Paper Evidence Map v0.1.0 鈥?reproducible first release`銆?
4. 姝ｆ枃澶嶅埗 `docs/releases/v0.1.0.md`銆?
5. 鍙戝竷鍚庨€愰」娴嬭瘯 README 涓殑閾炬帴鍜屼笅杞藉悗鐨勪袱鏉￠獙璇佸懡浠ゃ€?

## 5. 鐪熸鐨勪笅杞藉娴?

鐢ㄥ彟涓€涓复鏃剁洰褰曢噸鏂板厠闅嗗叕寮€浠撳簱锛?

```bash
git clone https://github.com/DaveKingh/paper-evidence-map.git
cd paper-evidence-map
python scripts/validate.py
python scripts/validate.py --response examples/synthetic/expected-output.md
```

鐒跺悗浠?GitHub 椤甸潰鐩存帴鎵撳紑涓枃 Prompt锛屽鍒跺埌涓€涓叏鏂扮殑 ChatGPT Project锛屼笂浼犲悎鎴愯鏂囧苟鍙戦€佲€滅涓€杞€濄€傚彧鏈夆€滈噸鏂颁笅杞?+ 鏂?Project鈥濋兘鎴愬姛锛岄涓増鏈墠绠楃湡姝ｅ彲澶嶇幇銆?


