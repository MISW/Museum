###### tags: `MIS.W` `misw-museum`

# misw-museum

## Models

### User

- id
- username
- first_name
- email
- generation
- association
- image
- description
- is_admin

### Model

#### DevelopmentInf(成果物情報テーブル)

- id (ゲームID，int型)
- title （ゲームタイトル，string型）
- description （ゲームの説明，string型）
- user_id （申請者情報，Forign Key）
- user_ids (共同開発者)
- association (研究会)
- status （ゲームタイトル，int型）
- is_public (boolean)
- link_id （ファイル配列，string型，linkInfのidを「1,2,3」みたいな形式で管理する）
- submitted_at（初回申請日時,DateTime型）
- updateded_at（更新日時,DateTime型）

#### linkInf

- id
- type (ファイルの種類、画像、音声、動画、URL(Windows，iOS，Android，その他)
- link (string)
- file (FileField)
