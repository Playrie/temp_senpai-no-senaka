class CreateFollows < ActiveRecord::Migration[6.0]
  def change
    create_table :follows do |t|
      t.integer :from_kerbero_id
      t.integer :to_kerbero_id

      t.timestamps
    end
  end
end
